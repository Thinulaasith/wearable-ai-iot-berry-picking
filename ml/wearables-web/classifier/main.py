import argparse
import json
import re
from pathlib import Path

from config import (
    DEFAULT_MODEL_CHOICE,
    MODEL_CHOICES,
    FRAMES_PER_SECOND,
    TEST_SIZE,
    RANDOM_STATE,
    RF_PARAMS,
    XGB_PARAMS,
    XGB_BINARY_PARAMS,
)

from preprocessing import create_training_data_from_merged

from train import (
    train_flat,
    train_hierarchical,
)

ARCHITECTURE_CHOICES = ("flat", "hierarchical", "both")


# ===================================================
# Study setup
# ===================================================


def _next_study_dir(studies_root: Path) -> Path:
    """
    Find the next study number and create its directory.

    studies/
        study_1/
        study_2/
        study_3/
    """

    studies_root.mkdir(parents=True, exist_ok=True)

    pattern = re.compile(r"^study_(\d+)$")

    max_study = 0

    for path in studies_root.iterdir():
        if not path.is_dir():
            continue

        match = pattern.match(path.name)

        if match:
            study_number = int(match.group(1))
            max_study = max(max_study, study_number)

    study_dir = studies_root / f"study_{max_study + 1}"

    study_dir.mkdir()

    return study_dir


def _create_study_folders(
    study_dir: Path,
    architecture: str,
) -> None:
    """
    Create the folders needed by the selected architectures.
    """

    (study_dir / "results").mkdir()

    if architecture in ("flat", "both"):
        (study_dir / "flat").mkdir()

    if architecture in ("hierarchical", "both"):
        (study_dir / "hierarchical").mkdir()


# ===================================================
# Study configuration
# ===================================================


def _save_study_config(
    study_dir: Path,
    merged_dir: Path,
    architecture: str,
    model: str,
    fps: int,
) -> None:

    config = {
        "study": study_dir.name,
        "dataset": {
            "source": str(merged_dir),
            "frames_per_second": fps,
            "training_data": "training_data.csv",
        },
        "experiment": {
            "architecture": architecture,
            "model": model,
            "test_size": TEST_SIZE,
            "random_state": RANDOM_STATE,
        },
        "model_parameters": {
            "random_forest": RF_PARAMS,
            "xgboost": XGB_PARAMS,
        },
    }

    config_path = study_dir / "config.json"

    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)


# ===================================================
# CLI
# ===================================================


def parse_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(description="Run activity classification study")

    parser.add_argument(
        "activity",
        help="Folder containing the merged CSV files",
    )

    parser.add_argument(
        "--merged-root",
        default="merged",
        help="Root directory containing merged datasets",
    )

    parser.add_argument(
        "--studies-root",
        default="studies",
        help="Directory where studies are saved",
    )

    parser.add_argument(
        "--fps",
        type=int,
        default=FRAMES_PER_SECOND,
        help="Number of sensor rows per second",
    )

    parser.add_argument(
        "--architecture",
        choices=ARCHITECTURE_CHOICES,
        default="both",
        help="Architecture to train",
    )

    parser.add_argument(
        "--model",
        choices=MODEL_CHOICES,
        default=DEFAULT_MODEL_CHOICE,
        help="Model algorithm to train",
    )

    return parser.parse_args()


# ===================================================
# Main
# ===================================================


def main() -> None:

    args = parse_args()

    activity = args.activity.strip()

    if not activity:
        raise ValueError("Activity folder name cannot be empty.")

    merged_dir = Path(args.merged_root) / activity
    studies_root = Path(args.studies_root)

    if not merged_dir.exists():
        raise FileNotFoundError(f"Dataset directory does not exist: {merged_dir}")

    # ---------------------------------------------------
    # Create new study
    # ---------------------------------------------------

    study_dir = _next_study_dir(studies_root)

    _create_study_folders(
        study_dir,
        args.architecture,
    )

    print(f"[study] Created {study_dir}")

    # ---------------------------------------------------
    # Save configuration
    # ---------------------------------------------------

    _save_study_config(
        study_dir=study_dir,
        merged_dir=merged_dir,
        architecture=args.architecture,
        model=args.model,
        fps=args.fps,
    )

    # ---------------------------------------------------
    # Preprocessing
    # ---------------------------------------------------

    training_csv = study_dir / "training_data.csv"

    create_training_data_from_merged(
        merged_dir,
        args.fps,
        training_csv,
    )

    print("[done] Training data created.")

    # ---------------------------------------------------
    # Flat architecture
    # ---------------------------------------------------

    if args.architecture in ("flat", "both"):

        print("\n[study] Training flat architecture")

        train_flat(
            train_csv=training_csv,
            study_dir=study_dir,
            model=args.model,
        )

    # ---------------------------------------------------
    # Standard hierarchical architecture
    # ---------------------------------------------------

    if args.architecture in ("hierarchical", "both"):

        print("\n[study] Training hierarchical architecture")

        train_hierarchical(
            train_csv=training_csv,
            study_dir=study_dir,
            model=args.model,
        )

    print(f"\n[done] Study completed: {study_dir}")


if __name__ == "__main__":
    main()
