import glob
import os
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from scipy import integrate

FRAMES_PER_SECOND_DEFAULT = 30

ENGINEERED_COLS = ["X", "Y", "Z", "XY", "YZ", "ZX", "XYZ", "Roll", "Pitch"]

BODY_PARTS: List[str] = [
    "d_leg",
    "d_wrist",
]

WIDE_PREFIX_TO_TAG: Dict[str, str] = {
    "D_LEG": "d_leg",
    "D_WRIST": "d_wrist",
}


def _stats(s: pd.Series) -> Dict[str, float | int]:
    s = pd.to_numeric(s, errors="coerce").astype(float).fillna(0.0)
    return {
        "mean": float(s.mean()),
        "std": float(s.std(ddof=0)),
        "min": float(s.min()),
        "max": float(s.max()),
        "auc": (
            float(integrate.trapezoid(s.values))
            if len(s.values) > 1
            else float(s.sum())
        ),
        "peaks": int(len(find_peaks(s.values)[0])),
    }


def _compute_signals_basic(df_xyz: pd.DataFrame) -> pd.DataFrame:
    # expects Acc_X/Y/Z columns present
    out = pd.DataFrame(index=df_xyz.index)
    out["X"] = df_xyz["Acc_X"]
    out["Y"] = df_xyz["Acc_Y"]
    out["Z"] = df_xyz["Acc_Z"]
    out["XY"] = np.sqrt((df_xyz[["Acc_X", "Acc_Y"]] ** 2).mean(axis=1))
    out["YZ"] = np.sqrt((df_xyz[["Acc_Y", "Acc_Z"]] ** 2).mean(axis=1))
    out["ZX"] = np.sqrt((df_xyz[["Acc_Z", "Acc_X"]] ** 2).mean(axis=1))
    out["XYZ"] = np.sqrt((df_xyz[["Acc_X", "Acc_Y", "Acc_Z"]] ** 2).mean(axis=1))
    out["Roll"] = np.degrees(
        np.arctan2(
            df_xyz["Acc_Y"], np.sqrt(df_xyz["Acc_X"] ** 2 + df_xyz["Acc_Z"] ** 2)
        )
    )
    out["Pitch"] = np.degrees(
        np.arctan2(
            -df_xyz["Acc_X"], np.sqrt(df_xyz["Acc_Y"] ** 2 + df_xyz["Acc_Z"] ** 2)
        )
    )
    return out.reset_index(drop=True)


def _find_acc_triplet(
    columns: List[str], prefix_upper: str
) -> Tuple[str, str, str] | None:
    """
    In WIDE CSVs we expect columns like:
        <Prefix>_Acc_X, <Prefix>_Acc_Y, <Prefix>_Acc_Z
    Example: 'Forearm_Acc_X' or 'Upper_Leg_Acc_X'
    """
    up = [c.upper() for c in columns]
    cand_x = f"{prefix_upper}_ACC_X"
    cand_y = f"{prefix_upper}_ACC_Y"
    cand_z = f"{prefix_upper}_ACC_Z"
    try:
        ix = up.index(cand_x)
        iy = up.index(cand_y)
        iz = up.index(cand_z)
        return columns[ix], columns[iy], columns[iz]
    except ValueError:
        return None


def _extract_part_xyz(chunk: pd.DataFrame, part_tag: str) -> pd.DataFrame:
    """Given a 1-second window `chunk`, get Acc_X/Y/Z for a known body part tag from WIDE columns."""
    prefixes = [p for p, t in WIDE_PREFIX_TO_TAG.items() if t == part_tag]
    for pref in prefixes:
        trip = _find_acc_triplet(list(chunk.columns), pref)
        if trip:
            xcol, ycol, zcol = trip
            return pd.DataFrame(
                {
                    "Acc_X": pd.to_numeric(chunk[xcol], errors="coerce"),
                    "Acc_Y": pd.to_numeric(chunk[ycol], errors="coerce"),
                    "Acc_Z": pd.to_numeric(chunk[zcol], errors="coerce"),
                }
            ).reset_index(drop=True)

    raise ValueError(f"Missing accelerometer columns for body part: {part_tag}")


def _engineer_window_features_wide(chunk: pd.DataFrame) -> Dict[str, Any]:
    feats: Dict[str, Any] = {}
    for part in BODY_PARTS:
        part_xyz = _extract_part_xyz(chunk, part)
        sig = _compute_signals_basic(part_xyz)
        for col in ENGINEERED_COLS:
            st = _stats(sig[col])
            for suf, val in st.items():
                feats[f"{part}_{col}_{suf}"] = val
    return feats


def features_from_one_csv(path: str, frames_per_second: int) -> pd.DataFrame:
    """
    For a single wide CSV:
      - read the CSV
      - stride over 1s windows (fps rows)
      - action = majority(Activity) over that window
      - engineered stats per BODY_PARTS
    """
    df = pd.read_csv(path)

    if "Activity" not in df.columns:
        raise ValueError(f"{os.path.basename(path)}: missing 'Activity' column")

    rows = []
    n = len(df)
    for start in range(0, n, frames_per_second):
        chunk = df.iloc[start : start + frames_per_second]
        if len(chunk) < frames_per_second:
            continue

        label = int(chunk["Activity"].mode().iloc[0])

        feat_row: Dict[str, Any] = {"action": label}
        feat_row.update(_engineer_window_features_wide(chunk))
        rows.append(feat_row)

    return pd.DataFrame(rows, copy=False)


# TODO add expected CSV format for the input
def create_training_data_from_merged(
    merged_dir: Path, frames_per_second: int, out_csv: Path
) -> pd.DataFrame:
    files = sorted(glob.glob(str(merged_dir / "*.csv")))
    if not files:
        raise FileNotFoundError(f"No CSVs found under {merged_dir}")

    all_feat_dfs: List[pd.DataFrame] = []
    for f in files:
        feat_df = features_from_one_csv(f, frames_per_second)
        if not feat_df.empty:
            all_feat_dfs.append(feat_df)

    if not all_feat_dfs:
        raise RuntimeError(
            "No feature rows produced — check CSV schema / Activity values / window size."
        )

    merged = pd.concat(all_feat_dfs, ignore_index=True)

    # Stable column order
    feature_order: List[str] = []
    for part in BODY_PARTS:
        for col in ENGINEERED_COLS:
            for suf in ("mean", "std", "min", "max", "auc", "peaks"):
                feature_order.append(f"{part}_{col}_{suf}")
    merged = merged[["action"] + feature_order]

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(out_csv, index=False)
    print(
        f"[build] Wrote {out_csv} with {len(merged)} rows and {merged.shape[1]} columns."
    )
    print("[build] Label distribution:", merged["action"].value_counts().to_dict())
    return merged
