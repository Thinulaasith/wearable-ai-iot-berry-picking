import argparse
import glob
import os
import pickle
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from scipy import integrate
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# try:
#     from xgboost import XGBClassifier
#     _HAS_XGB = True
# except Exception:
#     _HAS_XGB = False

_HAS_XGB = False

FRAMES_PER_SECOND_DEFAULT = 30 

ENGINEERED_COLS = ["X", "Y", "Z", "XY", "YZ", "ZX", "XYZ", "Roll", "Pitch"]

BODY_PARTS: List[str] = ["forearm", "upper_leg", "upper_back", "upper_arm", "back", "left_wrist", "right_wrist", "wrist"]

WIDE_PREFIX_TO_TAG: Dict[str, str] = {
    "FOREARM": "forearm",
    "UPPER_LEG": "upper_leg",
    "UPPERLEG": "upper_leg",
    "UPPER_BACK": "upper_back",
    "UPPERBACK": "upper_back",
    "UPPER_ARM": "upper_arm",
    "UPPERARM": "upper_arm",
    "BACK": "back",
    "LEFT_WRIST": "left_wrist",
    "LEFTWRIST": "left_wrist",
    "RIGHT_WRIST": "right_wrist",
    "RIGHTWRIST": "right_wrist",
    "WRIST": "wrist"
}

def _normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
          .str.strip()
          .str.replace(r"\s+", "_", regex=True)
          .str.replace(r"[^0-9A-Za-z_]", "", regex=True)
    )
    return df

def _label_to_int(x: Any) -> int | None:
    """Accept 0/1/2 or strings {'idle','good','bad'} → 0/1/2. Return None if unknown."""
    if pd.isna(x):
        return None
    try:
        v = int(x)
        return v if v in (1, 2, 3, 4) else None
    except Exception:
        s = str(x).strip().lower()  
        m = { "Bending": 1, "Idle": 2, "Picking": 3, "Pushing": 4}    
        return m.get(s)

def _majority_label(series: pd.Series) -> int | None:
    s = series.map(_label_to_int).dropna()
    if s.empty:
        return None
    return int(s.value_counts().idxmax())

def _stats(s: pd.Series) -> Dict[str, float | int]:
    s = pd.to_numeric(s, errors="coerce").astype(float).fillna(0.0)
    return {
        "mean": float(s.mean()),
        "std":  float(s.std(ddof=0)),
        "min":  float(s.min()),
        "max":  float(s.max()),
        "auc":  float(integrate.trapezoid(s.values)) if len(s.values) > 1 else float(s.sum()),
        "peaks": int(len(find_peaks(s.values)[0])),
    }

def _compute_signals_basic(df_xyz: pd.DataFrame) -> pd.DataFrame:
    # expects Acc_X/Y/Z columns present
    req = {"Acc_X", "Acc_Y", "Acc_Z"}
    if not req.issubset(df_xyz.columns):
        return pd.DataFrame(columns=ENGINEERED_COLS)
    out = pd.DataFrame(index=df_xyz.index)
    out["X"] = df_xyz["Acc_X"]
    out["Y"] = df_xyz["Acc_Y"]
    out["Z"] = df_xyz["Acc_Z"]
    out["XY"]  = np.sqrt((df_xyz[["Acc_X", "Acc_Y"]]**2).mean(axis=1))
    out["YZ"]  = np.sqrt((df_xyz[["Acc_Y", "Acc_Z"]]**2).mean(axis=1))
    out["ZX"]  = np.sqrt((df_xyz[["Acc_Z", "Acc_X"]]**2).mean(axis=1))
    out["XYZ"] = np.sqrt((df_xyz[["Acc_X", "Acc_Y", "Acc_Z"]]**2).mean(axis=1))
    out["Roll"]  = np.degrees(np.arctan2(df_xyz["Acc_Y"], np.sqrt(df_xyz["Acc_X"]**2 + df_xyz["Acc_Z"]**2)))
    out["Pitch"] = np.degrees(np.arctan2(-df_xyz["Acc_X"], np.sqrt(df_xyz["Acc_Y"]**2 + df_xyz["Acc_Z"]**2)))
    return out.reset_index(drop=True)

def _find_acc_triplet(columns: List[str], prefix_upper: str) -> Tuple[str, str, str] | None:
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
        ix = up.index(cand_x); iy = up.index(cand_y); iz = up.index(cand_z)
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
            return pd.DataFrame({
                "Acc_X": pd.to_numeric(chunk[xcol], errors="coerce"),
                "Acc_Y": pd.to_numeric(chunk[ycol], errors="coerce"),
                "Acc_Z": pd.to_numeric(chunk[zcol], errors="coerce"),
            }).reset_index(drop=True)
    return pd.DataFrame(columns=["Acc_X", "Acc_Y", "Acc_Z"])

def _engineer_window_features_wide(chunk: pd.DataFrame) -> Dict[str, Any]:
    feats: Dict[str, Any] = {}
    for part in BODY_PARTS:
        part_xyz = _extract_part_xyz(chunk, part)
        if part_xyz.empty:
            for col in ENGINEERED_COLS:
                for suf in ("mean", "std", "min", "max", "auc", "peaks"):
                    feats[f"{part}_{col}_{suf}"] = 0.0 if suf != "peaks" else 0
            continue
        sig = _compute_signals_basic(part_xyz)
        for col in ENGINEERED_COLS:
            if col not in sig.columns or sig[col].empty:
                for suf in ("mean", "std", "min", "max", "auc", "peaks"):
                    feats[f"{part}_{col}_{suf}"] = 0.0 if suf != "peaks" else 0
                continue
            st = _stats(sig[col])
            for suf, val in st.items():
                feats[f"{part}_{col}_{suf}"] = val
    return feats

def features_from_one_csv(path: str, frames_per_second: int) -> pd.DataFrame:
    """
    For a single wide CSV:
      - normalize cols
      - stride over 1s windows (fps rows)
      - action = majority(Activity) over that window
      - engineered stats per BODY_PARTS (zeros if part not present in file)
    """
    df = pd.read_csv(path)
    df = _normalize_columns(df)

    if "Activity" not in df.columns:
        raise ValueError(f"{os.path.basename(path)}: missing 'Activity' column")

    rows = []
    n = len(df)
    for start in range(0, n, frames_per_second):
        chunk = df.iloc[start:start + frames_per_second]
        if len(chunk) < frames_per_second:
            continue

        label = _majority_label(chunk["Activity"])
        if label is None:
            continue

        feat_row: Dict[str, Any] = {"action": int(label)}
        feat_row.update(_engineer_window_features_wide(chunk))
        rows.append(feat_row)

    return pd.DataFrame(rows, copy=False)

def create_training_data_from_merged(merged_dir: Path, frames_per_second: int, out_csv: Path) -> pd.DataFrame:
    files = sorted(glob.glob(str(merged_dir / "*.csv")))
    if not files:
        raise FileNotFoundError(f"No CSVs found under {merged_dir}")

    all_feat_dfs: List[pd.DataFrame] = []
    for f in files:
        feat_df = features_from_one_csv(f, frames_per_second)
        if not feat_df.empty:
            all_feat_dfs.append(feat_df)

    if not all_feat_dfs:
        raise RuntimeError("No feature rows produced — check CSV schema / Activity values / window size.")

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
    print(f"[build] Wrote {out_csv} with {len(merged)} rows and {merged.shape[1]} columns.")
    print("[build] Label distribution:", merged["action"].value_counts().to_dict())
    return merged


# ========= Model training =========

def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def train_random_forest(train_csv: Path, out_model: Path) -> tuple[RandomForestClassifier, float]:
    df = pd.read_csv(train_csv)
    X = df.drop(columns=["action"])
    y = df["action"].astype(int)

    print("[train] Label distribution:", y.value_counts().to_dict())

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=400,
        random_state=42,
        n_jobs=-1,
        class_weight="balanced_subsample",
        max_depth=None,
        min_samples_leaf=1
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = float(accuracy_score(y_test, y_pred))

    print(f"[train] RandomForest Accuracy: {acc:.4f}")
    print("[train] Confusion matrix:\n", confusion_matrix(y_test, y_pred))
    print("[train] Report:\n", classification_report(y_test, y_pred, digits=3))

    ensure_dir(out_model.parent)
    with open(out_model, "wb") as f:
        pickle.dump(model, f)
    print(f"[save] RandomForest → {out_model}")
    return model, acc

def train_xgb_if_available(train_csv: Path, out_model: Path) -> float | None:
    if not _HAS_XGB:
        print("[train] XGBoost not installed; skipping.")
        return None

    df = pd.read_csv(train_csv)
    X = df.drop(columns=["action"])
    y = df["action"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    xgb = XGBClassifier(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.9,
        colsample_bytree=0.9,
        eval_metric="mlogloss",
        random_state=42
    )
    xgb.fit(X_train, y_train)
    y_pred = xgb.predict(X_test)
    acc = float(accuracy_score(y_test, y_pred))
    print(f"[train] XGBoost Accuracy: {acc:.4f}")

    ensure_dir(out_model.parent)
    with open(out_model, "wb") as f:
        pickle.dump(xgb, f)
    print(f"[save] XGBoost → {out_model}")
    return acc

# ========= Versioned filenames =========

def _scan_existing_versions(models_dir: Path, activity: str, alg: str) -> int:
    """
    Find the highest version for files like:
      rf_<activity>_v12.pkl  or  xgb_<activity>_v7.joblib
    Returns max N (0 if none).
    """
    if not models_dir.exists():
        return 0
    pat = re.compile(rf"^{re.escape(alg)}_{re.escape(activity)}_v(\d+)\.(pkl|joblib)$", re.IGNORECASE)
    max_n = 0
    for p in models_dir.iterdir():
        m = pat.match(p.name)
        if m:
            try:
                n = int(m.group(1))
                if n > max_n:
                    max_n = n
            except ValueError:
                pass
    return max_n

def _next_versioned_name(models_dir: Path, activity: str, alg: str, ext: str = "pkl") -> Path:
    """
    Compute next filename with incremented numeric suffix:
      <models_dir>/<alg>_<activity>_v<N+1>.<ext>
    Example: rf_pickup_v3.pkl
    """
    current = _scan_existing_versions(models_dir, activity, alg)
    nxt = current + 1 if current >= 1 else 1
    return models_dir / f"{alg}_{activity}_v{nxt}.{ext}"

# ========= CLI =========

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Train activity-specific model from wide CSVs")
    p.add_argument("activity", help="Activity name (e.g. pickup, shelf, spray)")
    p.add_argument("--merged-root", default="merged", help="Root folder containing per-activity subfolders")
    p.add_argument("--models-root", default="models", help="Root folder to write per-activity models")
    p.add_argument("--fps", type=int, default=FRAMES_PER_SECOND_DEFAULT, help="Rows per 1-second window")
    p.add_argument("--no-xgb", action="store_true", help="Skip XGBoost training")
    p.add_argument(
        "--fixed-name",
        action="store_true",
        help="Use fixed filenames rf_<activity>.pkl / xgb_<activity>.pkl instead of auto-versioning."
    )
    return p.parse_args()

def main() -> None:
    args = parse_args()
    activity: str = args.activity.strip()
    if not activity:
        raise SystemExit("Activity must be a non-empty string, e.g. `pickup`.")

    merged_dir = Path(args.merged_root) / activity
    models_dir = Path(args.models_root) / activity
    train_csv  = Path(f"training_data_{activity}.csv")

    # Filenames:
    #  - default (auto-version): rf_<activity>_vN.pkl, xgb_<activity>_vN.pkl
    #  - with --fixed-name     : rf_<activity>.pkl,   xgb_<activity>.pkl
    if args.fixed_name:
        rf_model_path  = models_dir / f"rf_{activity}.pkl"
        xgb_model_path = models_dir / f"xgb_{activity}.pkl"
        auto_versioning = False
    else:
        rf_model_path  = _next_versioned_name(models_dir, activity, "rf", "pkl")
        xgb_model_path = _next_versioned_name(models_dir, activity, "xgb", "pkl")
        auto_versioning = True

    print(f"[config] activity        : {activity}")
    print(f"[config] merged input    : {merged_dir}")
    print(f"[config] models output   : {models_dir}")
    print(f"[config] fps/window size : {args.fps} rows")
    print(f"[config] auto-versioning : {'ON' if auto_versioning else 'OFF (fixed names)'}")
    print(f"[config] RF model file   : {rf_model_path}")
    if not args.no_xgb:
        print(f"[config] XGB model file  : {xgb_model_path}")

    # 1) Build features
    _ = create_training_data_from_merged(merged_dir, args.fps, train_csv)
    print("[done] Training data created.")

    # 2) Train RF
    ensure_dir(models_dir)
    _, acc = train_random_forest(train_csv, rf_model_path)
    print("[done] RandomForest model saved.")

    # 3) Optional XGB
    if not args.no_xgb:
        _ = train_xgb_if_available(train_csv, xgb_model_path)

if __name__ == "__main__":
    main()
