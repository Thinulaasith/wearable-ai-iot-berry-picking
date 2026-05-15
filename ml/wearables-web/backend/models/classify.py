# classifier_runner.py
import time
import pandas as pd
import numpy as np
import joblib
import threading

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from scipy.signal import find_peaks
from scipy import integrate

INFLUXDB_URL = "http://localhost:8086"
INFLUXDB_TOKEN = "dPKgz_WNL-6iJez-V5jiXZzsgcFcikYZAx5F8wsMD1mc2b58xgxYImWWk4sY3xPryWx_oXV7tS6HzU2qOkc76Q=="
INFLUXDB_ORG = "swinburne"
INFLUXDB_BUCKET = "sensor_data"
INFLUXDB_QUERY_MEASUREMENT = "sensor_data"
INFLUXDB_RESULT_MEASUREMENT = "classification"

def run_classifier(activity: str, timeout: int, stop_event: threading.Event):
    print(f"[classifier] Running for activity='{activity}' for {timeout}s")
    client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
    query_api = client.query_api()
    write_api = client.write_api(write_options=SYNCHRONOUS)
    model = joblib.load(f"rfc_{activity}_model.pkl")

    def compute_signals(df):
        new_df = pd.DataFrame()
        new_df['X'] = df["Acc_X"]
        new_df['Y'] = df["Acc_Y"]
        new_df['Z'] = df["Acc_Z"]
        new_df['XY'] = np.sqrt((df[['Acc_X', 'Acc_Y']]**2).mean(axis=1))
        new_df['YZ'] = np.sqrt((df[['Acc_Y', 'Acc_Z']]**2).mean(axis=1))
        new_df['ZX'] = np.sqrt((df[['Acc_Z', 'Acc_X']]**2).mean(axis=1))
        new_df['XYZ'] = np.sqrt((df[['Acc_X', 'Acc_Y', 'Acc_Z']]**2).mean(axis=1))
        new_df["Roll"] = np.degrees(np.arctan2(df['Acc_Y'], np.sqrt(df['Acc_X']**2 + df['Acc_Z']**2)))
        new_df["Pitch"] = np.degrees(np.arctan2(-df['Acc_X'], np.sqrt(df['Acc_Y']**2 + df['Acc_Z']**2)))
        return new_df.reset_index(drop=True)

    def compute_features(df):
        feats = {}
        for col in df.columns:
            feats[f"{col}_mean"] = df[col].mean()
            feats[f"{col}_std"] = df[col].std()
            feats[f"{col}_min"] = df[col].min()
            feats[f"{col}_max"] = df[col].max()
            feats[f"{col}_auc"] = integrate.trapezoid(df[col])
            feats[f"{col}_peaks"] = len(find_peaks(df[col])[0])
        return feats

    start = time.time()
    while time.time() - start < timeout and not stop_event.is_set():
        query = f'''
        from(bucket: "{INFLUXDB_BUCKET}")
        |> range(start: -1250ms)
        |> filter(fn: (r) => r._measurement == "{INFLUXDB_QUERY_MEASUREMENT}")
        |> filter(fn: (r) => r._field == "Acc_X" or r._field == "Acc_Y" or r._field == "Acc_Z")
        |> sort(columns: ["_time"])
        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
        '''

        df = query_api.query_data_frame(query)
        if isinstance(df, list) and df:
            df = pd.concat(df)
        if df.empty:
            time.sleep(1)
            continue

        df.set_index("_time", inplace=True)
        df_arm = df[df["body_part"] == "arm"][["Acc_X", "Acc_Y", "Acc_Z"]].reset_index(drop=True)
        df_back = df[df["body_part"] == "back"][["Acc_X", "Acc_Y", "Acc_Z"]].reset_index(drop=True)

        if df_arm.empty or df_back.empty:
            continue

        arm_signals = compute_signals(df_arm)
        back_signals = compute_signals(df_back)
        arm_feats = compute_features(arm_signals)
        back_feats = compute_features(back_signals)

        combined = {f"Right Lower Arm_{k}": v for k, v in arm_feats.items()}
        combined.update({f"Back_{k}": v for k, v in back_feats.items()})
        df_features = pd.DataFrame([combined])
        df_features = df_features.reindex(columns=model.feature_names_in_, fill_value=0.0)

        pred = int(model.predict(df_features)[0])
        print(f"[classifier] Prediction: {pred}")

        write_api.write(
            bucket=INFLUXDB_BUCKET,
            org=INFLUXDB_ORG,
            record=Point(INFLUXDB_RESULT_MEASUREMENT).field("action", pred).time(time.time_ns(), WritePrecision.NS)
        )

        time.sleep(1.25)

    print("[classifier] Finished classification.")
