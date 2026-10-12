import pandas as pd
from pathlib import Path
from config import (
    BENDING,
    IDLE,
    GOOD_PICKING,
    BAD_PICKING,
    PUSHING,
    SENSOR_POSITIONS,
)

STUDY_NAME = "2_Sensor_5_activities"
INPUT_PATH = Path(__file__).resolve().parent / "input_datasets"
OUTPUT_PATH = Path(f"merged/{STUDY_NAME}")
SENSOR_COUNT = len(SENSOR_POSITIONS)

PEOPLE = [
    "Hiruni",
    "Hiruni_1",
    "Hiruni_2",
    "Mineth",
    "Mineth_1",
    "Mineth_2",
    "Sineth",
    "Thanushka_1",
    "Thinula",
    "Thinula_1",
    "Thinula_2",
]

ACTIVITIES = {
    "bending": BENDING,
    "idle": IDLE,
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

    wrist_aliases = ("r_wrist", "l_wrist", "d_wrist")

    for alias in wrist_aliases:
        if file_stem == alias or file_stem.startswith(f"{alias}_"):
            return "D_Wrist"

    for sensor_position in SENSOR_POSITIONS:
        sensor_key = sensor_position.casefold()

        if file_stem == sensor_key or file_stem.startswith(f"{sensor_key}_"):
            return sensor_position

    raise ValueError(f"Unknown sensor placement: {file_path.name}")


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


def get_sync_status(file_path: Path) -> str | None:
    """
    Read the metadata section of a sensor CSV and return its SyncStatus.
    Returns None if SyncStatus cannot be found.
    """

    with open(file_path, "r", encoding="utf-8-sig") as f:
        for _ in range(11):
            line = f.readline()

            if not line:
                break

            key, _, value = line.partition(",")

            if key.strip().rstrip(":").casefold() == "syncstatus":
                return value.strip()

    return None


# def validate_all_sensor_sync(
#     input_path: Path,
#     people: list[str],
#     activities: dict[str, int],
# ) -> None:
#     """
#     Check all sensor CSV files that will be used by the merger.

#     If any files are unsynced or missing SyncStatus metadata,
#     report all of them and stop before merging begins.
#     """

#     sync_problems = []

#     for person in people:
#         person_path = input_path / person

#         if not person_path.exists():
#             continue

#         for activity in activities:
#             prefix = f"{person}_{activity}".casefold()

#             activity_folders = [
#                 folder
#                 for folder in person_path.iterdir()
#                 if folder.is_dir() and folder.name.casefold().startswith(prefix)
#             ]

#             for activity_folder in activity_folders:
#                 for sensor_file in activity_folder.glob("*.csv"):

#                     sync_status = get_sync_status(sensor_file)

#                     if sync_status is None or sync_status.casefold() != "synced":
#                         sync_problems.append(
#                             {
#                                 "person": person,
#                                 "activity": activity_folder.name,
#                                 "file": sensor_file.name,
#                                 "status": sync_status or "SyncStatus missing",
#                             }
#                         )

#     if sync_problems:
#         print("\nSYNC VALIDATION FAILED")
#         print("=" * 80)

#         for problem in sync_problems:
#             print(
#                 f"{problem['person']} | "
#                 f"{problem['activity']} | "
#                 f"{problem['file']} | "
#                 f"Status: {problem['status']}"
#             )

#         print(f"\nFound {len(sync_problems)} sensor file(s) " "that are not synced.")

#         raise RuntimeError("Merging stopped because unsynced sensor files were found.")

#     print("[sync] All sensor files are synced.")


# validate_all_sensor_sync(
#     INPUT_PATH,
#     PEOPLE,
#     ACTIVITIES,
# )

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

summary = {activity: {"People": set(), "Collections": {}} for activity in ACTIVITIES}

folders = sorted(INPUT_PATH.iterdir())

for person in PEOPLE:
    person_path = INPUT_PATH / person

    if not person_path.exists():
        print(f"Person folder not found: {person_path.resolve()}")
        continue

    person_data = []

    for activity, activity_label in ACTIVITIES.items():
        prefix = f"{person}_{activity}".casefold()

        activity_folders = sorted(
            [
                folder
                for folder in person_path.iterdir()
                if folder.is_dir() and folder.name.casefold().startswith(prefix)
            ]
        )

        if not activity_folders:
            continue

        for activity_folder in activity_folders:
            sensor_files = sorted(activity_folder.glob("*.csv"))

            # Check the exact number of sensors
            if len(sensor_files) != SENSOR_COUNT:
                raise ValueError(
                    f"{activity_folder} contains only "
                    f"{len(sensor_files)} sensor files. "
                    f"Expected {SENSOR_COUNT} sensor files."
                )

            sensor_data = {}

            for sensor_file in sensor_files:
                sensor_key = get_sensor_key(sensor_file)
                sensor_df = read_sensor_file(sensor_file, sensor_key)

                sensor_data[sensor_key] = sensor_df

            # Check whether every sensor has the same row count
            sensor_frames = list(sensor_data.values())

            trial_df = sensor_frames[0]

            for sensor_df in sensor_frames[1:]:
                trial_df = trial_df.merge(
                    sensor_df, on="SampleTimeFine", how="inner", validate="one_to_one"
                )

            trial_df = trial_df.sort_values("SampleTimeFine").reset_index(drop=True)

            if trial_df.empty:
                raise ValueError(
                    f"No matching SampleTimeFine values found in " f"{activity_folder}"
                )

            original_row_counts = {
                sensor_key: len(sensor_df)
                for sensor_key, sensor_df in sensor_data.items()
            }

            discarded_rows = {
                sensor_key: row_count - len(trial_df)
                for sensor_key, row_count in original_row_counts.items()
            }

            if any(count > 0 for count in discarded_rows.values()):
                print(
                    f"Warning: unmatched samples removed from "
                    f"{activity_folder.name}: {discarded_rows}"
                )

            # Add metadata
            trial_df["Activity"] = activity_label

            person_data.append(trial_df)

            # Record this successfully processed collection
            summary[activity]["People"].add(person)
            summary[activity]["Collections"].setdefault(person, [])
            summary[activity]["Collections"][person].append(activity_folder.name)

    # Vertically combine this person's activity trials
    if person_data:
        person_df = pd.concat(person_data, ignore_index=True)
        person_df.to_csv(OUTPUT_PATH / f"{person}.csv", index=False)


summary_rows = []

for activity in ACTIVITIES:
    activity_summary = summary[activity]
    collections_by_person = []

    for person in sorted(activity_summary["Collections"]):
        collection_folders = sorted(activity_summary["Collections"][person])

        indexed_collections = ", ".join(
            f"{index}. {folder_name}"
            for index, folder_name in enumerate(collection_folders, start=1)
        )

        collections_by_person.append(f"{person}: {indexed_collections}")

    total_collections = sum(
        len(collection_folders)
        for collection_folders in activity_summary["Collections"].values()
    )

    summary_rows.append(
        {
            "Activity": activity,
            "Number of People": len(activity_summary["People"]),
            "People": ", ".join(sorted(activity_summary["People"])),
            "Number of Collections": total_collections,
            "Collections by Person": " | ".join(collections_by_person),
        }
    )

summary_df = pd.DataFrame(summary_rows)

# Compact summary
print("\nACTIVITY SUMMARY")
print("=" * 70)

print(
    summary_df[
        [
            "Activity",
            "Number of People",
            "People",
            "Number of Collections",
        ]
    ].to_string(index=False)
)

# Detailed collections
print("\nCOLLECTION DETAILS")
print("=" * 70)

for activity in ACTIVITIES:
    activity_summary = summary[activity]

    print(f"\n{activity.replace('_', ' ').title()}")
    print("-" * 50)

    for person in sorted(activity_summary["Collections"]):
        folders = sorted(activity_summary["Collections"][person])

        print(f"{person}:")
        for index, folder in enumerate(folders, start=1):
            print(f"  {index}. {folder}")
