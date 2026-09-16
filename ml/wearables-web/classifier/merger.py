import pandas as pd
from pathlib import Path

from config import BENDING, IDLE, GOOD_PICKING, BAD_PICKING, PUSHING, SENSOR_POSITIONS

STUDY_NAME = "2_Sensor_5_activities"

INPUT_PATH = Path(__file__).resolve().parent / "input_datasets"
OUTPUT_PATH = Path(f"merged/{STUDY_NAME}")

PEOPLE = [
    "Hiruni",
    "Mineth",
    "Sineth",
    "Thanushka",
    "Tanushka",
    "Thinula",
]

ACTIVITIES = {
    "bending": BENDING,
    "idle": IDLE,
    "picking_good": GOOD_PICKING,
    "picking_bad": BAD_PICKING,
    "good_picking": GOOD_PICKING,
    "bad_picking": BAD_PICKING,
    "pushing": PUSHING,
}

ACCELEROMETER_COLUMNS = {
    "FreeAcc_X": "Acc_X",
    "FreeAcc_Y": "Acc_Y",
    "FreeAcc_Z": "Acc_Z",
}


def get_sensor_key(file_path: Path) -> str:
    file_stem = file_path.stem.casefold()

    for sensor_position in SENSOR_POSITIONS:
        sensor_key = sensor_position.casefold()

        if file_stem == sensor_key or file_stem.startswith(f"{sensor_key}_"):
            return sensor_position

    raise ValueError(f"Unknown sensor placement: {file_path}")


def read_sensor_file(file_path: Path, sensor_key: str) -> pd.DataFrame:

    df = pd.read_csv(
        file_path,
        skiprows=11,
        usecols=["SampleTimeFine", *ACCELEROMETER_COLUMNS.keys()],
    )

    renamed_columns = {
        original_name: f"{sensor_key}_{new_name}"
        for original_name, new_name in ACCELEROMETER_COLUMNS.items()
    }

    return df.rename(columns=renamed_columns)


OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

sessions = sorted(INPUT_PATH.iterdir())
sessions = [s for s in sessions if s.is_dir()]

for session in sessions:
    folders = sorted(session.iterdir())

    person_folders = [f for f in folders if f.is_dir()]
    checked_people = []

    for person in PEOPLE:
        person_df = pd.DataFrame()
        person_path = session / person

        if not person_path.exists():
            continue

        checked_people.append(person)

        activity_folders = [f for f in person_path.iterdir() if f.is_dir()]

        checked_activity_folders = []

        for activity, activity_code in ACTIVITIES.items():
            prefix = f"{person}_{activity}".casefold()

            matching_folders = [
                f for f in activity_folders if f.name.casefold().startswith(prefix)
            ]

            checked_activity_folders.extend(matching_folders)

            for folder in matching_folders:
                sensor_data = None
                sensor_files = sorted(folder.glob("*.csv"))

                if not sensor_files:
                    raise ValueError(f"No sensor files found in {folder}")

                for sensor_file in sensor_files:

                    sensor_key = get_sensor_key(sensor_file)
                    sensor_df = read_sensor_file(sensor_file, sensor_key)

                    if sensor_data is None:
                        sensor_data = sensor_df
                    else:
                        count_before_merge = len(sensor_data)

                        sensor_data = pd.merge(
                            sensor_data,
                            sensor_df,
                            on="SampleTimeFine",
                            how="inner",
                            validate="one_to_one",
                        )

                        count_after_merge = len(sensor_data)

                        if count_before_merge - count_after_merge > 2:
                            print(
                                f"Warning: SampleTimeFine mismatch in "
                                f"{session.name} \\ {person} \\ {folder.name}. "
                                f"Gap of {count_before_merge - count_after_merge} rows."
                            )

                sensor_data["Activity"] = activity_code
                person_df = pd.concat([person_df, sensor_data], ignore_index=True)

        if not person_df.empty:
            person_df.to_csv(
                OUTPUT_PATH / f"{session.name}_{person}.csv",
                index=False,
            )

        missing_activities = set(activity_folders) - set(checked_activity_folders)

        if missing_activities:
            print(
                f"Warning: Unknown activity folders in `{session.name} / {person}`: "
                f"{[f.name for f in missing_activities]}"
            )

    if len(checked_people) != len(person_folders):
        skipped_people = set(f.name for f in person_folders) - set(checked_people)
        print(
            f"Warning: Unrecognized person folders in `{session.name}`: "
            f"{skipped_people}"
        )
