# classify.py
# Stream-to-Influx classifier runner.
# - Reads recent Acc_X/Y/Z for TWO body parts from Influx (INFLUX_QUERY_MEASUREMENT)
# - Engineers windowed features to match training
# - Resolves live body_part tags (e.g. 'forearm','upper_leg') to the model's
#   original family names (e.g. 'Forearm','Upper_Leg') so feature columns align
# - Writes predictions to INFLUX_RESULT_MEASUREMENT as field "action"
#
# Env (.env) REQUIRED:
#   INFLUX_URL
#   INFLUX_TOKEN
#   INFLUX_ORG
#   INFLUX_BUCKET
#   INFLUX_QUERY_MEASUREMENT    (what the streamer writes, e.g. "sensor_data")
#   INFLUX_RESULT_MEASUREMENT   (what we write, e.g. "classification")
#
# Optional:
#   MODEL_DIR  (defaults to ./models next to this file)

from __future__ import annotations

import math
import os
import re
import time
import threading
from pathlib import Path
from typing import Dict, Any, List, Tuple

import numpy as np
import pandas as pd
import joblib

from dotenv import load_dotenv
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from scipy.signal import find_peaks
from scipy import integrate

# ---------- ENV & CONFIG ----------
load_dotenv()


def getenv_str(name: str, default: str | None = None) -> str:
    v = os.getenv(name, default)
    if v is None or not str(v).strip():
        raise RuntimeError(f"Missing required env var: {name}")
    return str(v).strip()


INFLUXDB_URL = getenv_str("INFLUX_URL")
INFLUXDB_TOKEN = getenv_str("INFLUX_TOKEN")
INFLUXDB_ORG = getenv_str("INFLUX_ORG")
INFLUXDB_BUCKET = getenv_str("INFLUX_BUCKET")

INFLUXDB_QUERY_MEASUREMENT = getenv_str("INFLUX_QUERY_MEASUREMENT")
INFLUXDB_RESULT_MEASUREMENT = getenv_str("INFLUX_RESULT_MEASUREMENT")

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_MODEL_DIR = (BASE_DIR / "models").resolve()
MODEL_DIR = Path(os.getenv("MODEL_DIR", str(DEFAULT_MODEL_DIR))).resolve()

# Configurable parameters
WINDOW_SECONDS = 2
SENSOR_RATE_HZ = 30
BUFFER_SECONDS = 1
PREDICTION_INTERVAL_SECONDS = 1.0
MAX_UNMATCHED = 2
# ----------------

SAMPLES_PER_WINDOW = int(WINDOW_SECONDS * SENSOR_RATE_HZ)
EXPECTED_GAP_US = math.ceil(1_000_000 / SENSOR_RATE_HZ)
MAX_GAP_US = math.ceil(EXPECTED_GAP_US * 1.5)
QUERY_MS = int((WINDOW_SECONDS + BUFFER_SECONDS) * 1000)


def _log(msg: str) -> None:
    print(f"[classifier] {msg}", flush=True)


def to_snake(s: str) -> str:
    """
    Normalize strings like 'Right Lower Arm' or 'Upper-Leg' -> 'right_lower_arm' / 'upper_leg'
    """
    s = re.sub(r"[\s\-]+", "_", s.strip())
    s = re.sub(r"__+", "_", s)
    return s.lower()


def families_from_feature_names(cols: List[str]) -> List[str]:
    """
    Extract model 'family' prefixes from feature names:
      'Forearm_X_mean'        -> 'Forearm'
      'Upper_Leg_XYZ_std'     -> 'Upper_Leg'
      'Right Lower Arm_Pitch' -> 'Right Lower Arm'
    Assumes the last two underscore groups are <Signal>_<stat>.
    """
    fams: List[str] = []
    seen = set()
    for c in cols:
        parts = c.rsplit("_", 2)
        fam = parts[0] if len(parts) == 3 else c
        if fam not in seen:
            seen.add(fam)
            fams.append(fam)
    return fams


def model_family_maps(expected_cols: List[str]) -> Tuple[List[str], Dict[str, str]]:
    """
    Build both the raw family list (as stored in the model) and a map
    from normalized family -> raw family.
    Example:
      expected: ['Forearm_X_mean', 'Upper_Leg_XYZ_std', ...]
      returns:
        raw = ['Forearm','Upper_Leg', ...]
        norm_to_raw = {'forearm':'Forearm','upper_leg':'Upper_Leg', ...}
    """
    raw = families_from_feature_names(expected_cols)
    norm_to_raw = {to_snake(r): r for r in raw}
    return raw, norm_to_raw


ENGINEERED_COLS = ["X", "Y", "Z", "XY", "YZ", "ZX", "XYZ", "Roll", "Pitch"]


def compute_signals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Input df columns: Acc_X, Acc_Y, Acc_Z
    Output df columns: ENGINEERED_COLS
    """
    req = {"Acc_X", "Acc_Y", "Acc_Z"}
    missing = req.difference(df.columns)
    if missing:
        raise ValueError(f"compute_signals: missing columns {missing}")

    new_df = pd.DataFrame(index=df.index)
    ax, ay, az = df["Acc_X"], df["Acc_Y"], df["Acc_Z"]

    new_df["X"] = ax
    new_df["Y"] = ay
    new_df["Z"] = az
    new_df["XY"] = np.sqrt((df[["Acc_X", "Acc_Y"]] ** 2).mean(axis=1))
    new_df["YZ"] = np.sqrt((df[["Acc_Y", "Acc_Z"]] ** 2).mean(axis=1))
    new_df["ZX"] = np.sqrt((df[["Acc_Z", "Acc_X"]] ** 2).mean(axis=1))
    new_df["XYZ"] = np.sqrt((df[["Acc_X", "Acc_Y", "Acc_Z"]] ** 2).mean(axis=1))
    new_df["Roll"] = np.degrees(np.arctan2(ay, np.sqrt(ax**2 + az**2)))
    new_df["Pitch"] = np.degrees(np.arctan2(-ax, np.sqrt(ay**2 + az**2)))
    return new_df.reset_index(drop=True)


def _stats(s: pd.Series) -> Dict[str, float | int]:
    s = pd.to_numeric(s, errors="coerce").astype(float).fillna(0.0)
    return {
        "mean": float(s.mean()),
        "std": float(s.std(ddof=0)),
        "min": float(s.min()),
        "max": float(s.max()),
        "auc": (float(integrate.trapezoid(s.values)) if len(s.values) > 1 else float(s.sum())),
        "peaks": int(len(find_peaks(s.values)[0])),
    }


def compute_features(sig_df: pd.DataFrame) -> Dict[str, Any]:
    feats: Dict[str, Any] = {}
    for col in ENGINEERED_COLS:
        if col not in sig_df.columns or sig_df[col].empty:
            for suf, zero in (
                ("mean", 0.0),
                ("std", 0.0),
                ("min", 0.0),
                ("max", 0.0),
                ("auc", 0.0),
                ("peaks", 0),
            ):
                feats[f"{col}_{suf}"] = zero
            continue
        st = _stats(sig_df[col])
        for suf, val in st.items():
            feats[f"{col}_{suf}"] = val
    return feats


def build_flux(bucket: str, measurement: str, window_ms: int) -> str:
    """
    Pull last ~`window_ms` ms and pivot so we get Acc_X/Y/Z columns, plus tags (body_part).
    """
    return f"""
from(bucket: "{bucket}")
|> range(start: -{window_ms}ms)
|> filter(fn: (r) => r._measurement == "{measurement}")
|> filter(fn: (r) => r._field == "Acc_X" or r._field == "Acc_Y" or r._field == "Acc_Z" or r._field == "sample_time")
|> sort(columns: ["_time"])
|> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
"""


def to_dataframe(query_api, flux: str) -> pd.DataFrame:
    df = query_api.query_data_frame(flux)

    if isinstance(df, list):
        if not df:
            return pd.DataFrame()
        df = pd.concat(df, ignore_index=False, copy=False)

    value_cols = {"Acc_X", "Acc_Y", "Acc_Z"}
    if df.empty or not value_cols.issubset(df.columns):
        return pd.DataFrame()
    return df


def run_classifier(activity: str, timeout: int, stop_event: threading.Event, model_name: str) -> None:
    _log(f"Starting (activity='{activity}', timeout={timeout}s, model='{model_name}')")
    if not (INFLUXDB_URL.startswith("http://") or INFLUXDB_URL.startswith("https://")):
        raise RuntimeError(f"INFLUX_URL must start with http:// or https:// (got {INFLUXDB_URL})")

    client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
    query_api = client.query_api()
    write_api = client.write_api(write_options=SYNCHRONOUS)

    # Load model
    model_path = (MODEL_DIR / model_name).resolve()
    if not model_path.exists():
        contents = ", ".join(sorted([f.name for f in MODEL_DIR.glob("*")])) if MODEL_DIR.exists() else "<missing dir>"
        raise FileNotFoundError(f"Model not found: {model_path}\nMODEL_DIR={MODEL_DIR}\nContents={contents}")

    _log(f"Loading model: {model_path}")
    model = joblib.load(model_path)

    expected_cols = list(getattr(model, "feature_names_in_", []))
    if not expected_cols:
        _log("Warning: model has no 'feature_names_in_' — predictions may fail if columns mismatch.")

    if expected_cols:
        available_fams_raw, fam_norm_to_raw = model_family_maps(expected_cols)
        available_fams_norm = [to_snake(f) for f in available_fams_raw]
    else:
        available_fams_raw = ["Forearm", "Upper_Leg", "Upper_Back", "Upper_Arm", "Back"]
        available_fams_norm = [to_snake(f) for f in available_fams_raw]
        fam_norm_to_raw = {to_snake(f): f for f in available_fams_raw}

    _log(f"Model families discovered (raw): {available_fams_raw}")

    flux = build_flux(INFLUXDB_BUCKET, INFLUXDB_QUERY_MEASUREMENT, QUERY_MS)

    start = time.time()
    try:
        while (time.time() - start) < timeout and not stop_event.is_set():
            df = to_dataframe(query_api, flux)
            if df.empty:
                _log("No samples in window; sleeping …")
                time.sleep(PREDICTION_INTERVAL_SECONDS)
                continue

            if "_time" in df.columns:
                df.set_index("_time", inplace=True, drop=True)
                df.sort_index(inplace=True)

            if "body_part" not in df.columns:
                _log("No 'body_part' tag in rows; skipping window.")
                time.sleep(PREDICTION_INTERVAL_SECONDS)
                continue

            if "sample_time" not in df.columns:
                _log("WARNING: sample_time missing from InfluxDB")
                time.sleep(PREDICTION_INTERVAL_SECONDS)
                continue

            present_parts_norm = [to_snake(p) for p in pd.Series(df["body_part"]).dropna().unique().tolist()]
            present_parts_norm = sorted(present_parts_norm)[:2]
            if len(present_parts_norm) < 2:
                _log(f"Need 2 body parts; saw: {present_parts_norm or '[]'}")
                time.sleep(PREDICTION_INTERVAL_SECONDS * 0.5)
                continue

            def pick_two_norm(present_norm: List[str], avail_norm: List[str]) -> List[str]:
                fams = [p for p in present_norm if p in avail_norm]
                for f in avail_norm:
                    if len(fams) >= 2:
                        break
                    if f not in fams:
                        fams.append(f)
                return fams[:2]

            famA_norm, famB_norm = pick_two_norm(present_parts_norm, available_fams_norm)

            famA_raw = fam_norm_to_raw.get(famA_norm, available_fams_raw[0])
            famB_raw = fam_norm_to_raw.get(famB_norm, available_fams_raw[1 if len(available_fams_raw) > 1 else 0])

            _log(f"Window parts(norm)={present_parts_norm} → families(raw)='{famA_raw}', '{famB_raw}'")

            partA_norm, partB_norm = present_parts_norm[:2]
            cols = ["sample_time", "Acc_X", "Acc_Y", "Acc_Z"]

            # Extract sensor readings
            df_A = df.loc[to_snake_series(df["body_part"]) == partA_norm, cols].dropna().copy()

            df_B = df.loc[to_snake_series(df["body_part"]) == partB_norm, cols].dropna().copy()

            for sensor_df in (df_A, df_B):
                sensor_df["sample_time"] = sensor_df["sample_time"].astype("int64")
                sensor_df.drop_duplicates("sample_time", keep="last", inplace=True)

            # Join by synchronized timestamp
            paired = pd.merge(
                df_A,
                df_B,
                on="sample_time",
                how="inner",
                suffixes=("_A", "_B"),
                validate="one_to_one",
            ).sort_values("sample_time")

            # Require enough matched readings
            if len(paired) < SAMPLES_PER_WINDOW:
                _log(f"Insufficient matched pairs: {len(paired)}/{SAMPLES_PER_WINDOW}")
                time.sleep(PREDICTION_INTERVAL_SECONDS)
                continue

            # Latest 60 matched pairs
            window = paired.tail(SAMPLES_PER_WINDOW)

            start_ts = int(window["sample_time"].iloc[0])
            end_ts = int(window["sample_time"].iloc[-1])

            # Check for unmatched readings within the window
            a_times = set(df_A.loc[df_A["sample_time"].between(start_ts, end_ts), "sample_time"])
            b_times = set(df_B.loc[df_B["sample_time"].between(start_ts, end_ts), "sample_time"])

            unmatched = len(a_times ^ b_times)

            if unmatched > MAX_UNMATCHED:
                _log(f"WARNING: {unmatched} unmatched sensor readings")

            # Check consecutive timestamp gaps
            gaps = np.diff(window["sample_time"].to_numpy(dtype=np.int64))
            invalid_gaps = gaps[(gaps <= 0) | (gaps > MAX_GAP_US)]

            if len(invalid_gaps) > 0:
                _log(
                    f"WARNING: {len(invalid_gaps)} irregular gaps | "
                    f"Maximum: {gaps.max()} µs | Allowed: {MAX_GAP_US} µs"
                )

            _log(f"Window: {len(window)} pairs | " f"Unmatched: {unmatched} | " f"Max gap: {gaps.max()} µs")

            # Restore original feature engineering input format
            df_A = window[["Acc_X_A", "Acc_Y_A", "Acc_Z_A"]].copy()
            df_B = window[["Acc_X_B", "Acc_Y_B", "Acc_Z_B"]].copy()

            df_A.columns = ["Acc_X", "Acc_Y", "Acc_Z"]
            df_B.columns = ["Acc_X", "Acc_Y", "Acc_Z"]

            df_A.reset_index(drop=True, inplace=True)
            df_B.reset_index(drop=True, inplace=True)

            # Feature engineering

            feats_A = compute_features(compute_signals(df_A))
            feats_B = compute_features(compute_signals(df_B))

            combined: Dict[str, Any] = {f"{famA_raw}_{k}": v for k, v in feats_A.items()}
            combined.update({f"{famB_raw}_{k}": v for k, v in feats_B.items()})

            X = pd.DataFrame([combined])
            if expected_cols:
                X = X.reindex(columns=expected_cols, fill_value=0.0)

            pred = int(model.predict(X)[0])
            proba = getattr(model, "predict_proba", None)
            if callable(proba):
                p = np.round(proba(X)[0], 3).tolist()
                _log(f"Prediction: {pred} | " f"Classes={model.classes_.tolist()} | Proba={p}")
            else:
                _log(f"Prediction: {pred}")

            point = Point(INFLUXDB_RESULT_MEASUREMENT).field("action", pred).time(time.time_ns(), WritePrecision.NS)

            write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)

            time.sleep(PREDICTION_INTERVAL_SECONDS)

    finally:
        try:
            write_api.__del__()  # close underlying resources
        except Exception:
            pass
        try:
            client.__del__()
        except Exception:
            pass
        _log("Finished classification.")


def to_snake_series(s: pd.Series) -> pd.Series:
    return s.astype(str).map(to_snake)
