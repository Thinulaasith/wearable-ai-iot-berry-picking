import pickle
import pandas as pd

from typing import Any, Dict
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from evaluation import (
    evaluate_predictions,
    save_json,
    save_flat_report,
    save_hierarchical_report,
)
from config import (
    RF_PARAMS,
    XGB_PARAMS,
    ModelChoice,
    DEFAULT_MODEL_CHOICE,
    MODEL_CHOICES,
    BENDING,
    IDLE,
    GOOD_PICKING,
    BAD_PICKING,
    PUSHING,
    S1_BENDING,
    S1_IDLE,
    S1_PICKING,
    S1_PUSHING,
    S2_GOOD,
    S2_BAD,
    FINAL_TO_STAGE1,
    FINAL_TO_STAGE2,
    TEST_SIZE,
    RANDOM_STATE,
)


def chronological_stratified_split(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
):
    train_indices = []
    test_indices = []

    for label in y.unique():
        class_indices = y[y == label].index

        split_index = int(len(class_indices) * (1 - test_size))

        train_indices.extend(class_indices[:split_index])
        test_indices.extend(class_indices[split_index:])

    X_train = X.loc[train_indices]
    y_train = y.loc[train_indices]

    X_test = X.loc[test_indices]
    y_test = y.loc[test_indices]

    X_train = X_train.sample(frac=1, random_state=random_state)
    y_train = y_train.loc[X_train.index]

    X_test = X_test.sample(frac=1, random_state=random_state)
    y_test = y_test.loc[X_test.index]

    return X_train, X_test, y_train, y_test


def train_flat(
    train_csv: Path,
    study_dir: Path,
    model: ModelChoice = DEFAULT_MODEL_CHOICE,
) -> Dict[str, Dict[str, Any]]:
    """
    Train the flat activity classifier.

    model:
        "both" -> train Random Forest and XGBoost
        "rf"   -> train only Random Forest
        "xgb"  -> train only XGBoost
    """
    if model not in MODEL_CHOICES:
        raise ValueError("model must be 'both', 'rf', or 'xgb'")

    flat_dir = study_dir / "flat"
    results_dir = study_dir / "results"

    df = pd.read_csv(train_csv)
    X = df.drop(columns=["action"])
    y = df["action"].astype(int)

    print("[train] Label distribution:", y.value_counts().to_dict())

    X_train, X_test, y_train, y_test = chronological_stratified_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )

    results: Dict[str, Dict[str, Any]] = {}

    if model in ("both", "rf"):
        rf = RandomForestClassifier(**RF_PARAMS)

        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)

        rf_evaluation = evaluate_predictions(
            y_test,
            y_pred,
            "flat",
        )

        save_json(
            rf_evaluation,
            results_dir / "flat_rf_results.json",
        )

        save_flat_report(
            rf_evaluation,
            results_dir / "flat_rf_report.md",
            "Flat Architecture - Random Forest",
        )

        # Save the trained model
        rf_model_path = flat_dir / "rf.pkl"
        with open(rf_model_path, "wb") as f:
            pickle.dump(rf, f)

        results["rf"] = {
            "model": rf,
            "evaluation": rf_evaluation,
            "path": rf_model_path,
        }

    if model in ("both", "xgb"):
        xgb = XGBClassifier(**XGB_PARAMS)

        xgb.fit(X_train, y_train)
        y_pred = xgb.predict(X_test)

        xgb_evaluation = evaluate_predictions(
            y_test,
            y_pred,
            "flat",
        )

        save_json(
            xgb_evaluation,
            results_dir / "flat_xgb_results.json",
        )

        save_flat_report(
            xgb_evaluation,
            results_dir / "flat_xgb_report.md",
            "Flat Architecture - XGBoost",
        )

        xgb_model_path = flat_dir / "xgb.pkl"

        # Save the trained model
        with open(xgb_model_path, "wb") as f:
            pickle.dump(xgb, f)

        results["xgb"] = {
            "model": xgb,
            "evaluation": xgb_evaluation,
            "path": xgb_model_path,
        }

    return results


# ---------------------------------------------------
# Standard Hierarchical Artichitecture
# ---------------------------------------------------


def _predict_hierarchical(model1, model2, X: pd.DataFrame):
    """
    Run the complete hierarchical pipeline and return final 5-class predictions.
    """

    # Stage 1: Bending / Idle / Picking / Pushing
    stage1_pred = model1.predict(X)

    stage1_pred = pd.Series(stage1_pred, index=X.index)

    # Final predictions use the original 5-class label system.
    final_pred = pd.Series(index=X.index, dtype=int)

    # Stage 1 predictions that don't require Stage 2
    final_pred.loc[stage1_pred == S1_BENDING] = BENDING
    final_pred.loc[stage1_pred == S1_IDLE] = IDLE
    final_pred.loc[stage1_pred == S1_PUSHING] = PUSHING

    # Only samples predicted as Picking go to Stage 2
    picking_mask = stage1_pred == S1_PICKING

    if picking_mask.any():
        stage2_pred = model2.predict(X.loc[picking_mask])

        stage2_pred = pd.Series(
            stage2_pred,
            index=X.loc[picking_mask].index,
        )

        good_indices = stage2_pred.index[stage2_pred == S2_GOOD]
        bad_indices = stage2_pred.index[stage2_pred == S2_BAD]

        final_pred.loc[good_indices] = GOOD_PICKING
        final_pred.loc[bad_indices] = BAD_PICKING

    return final_pred.astype(int)


def train_hierarchical(
    train_csv: Path,
    study_dir: Path,
    model: ModelChoice = DEFAULT_MODEL_CHOICE,
) -> Dict[str, Dict[str, Any]]:
    """
    Train the standard hierarchical architecture.

    Stage 1:
        Bending / Idle / Picking / Pushing

    Stage 2:
        Good Picking / Bad Picking

    model:
        "both" -> train Random Forest and XGBoost
        "rf"   -> train only Random Forest
        "xgb"  -> train only XGBoost
    """

    if model not in MODEL_CHOICES:
        raise ValueError("model must be 'both', 'rf', or 'xgb'")

    hierarchical_dir = study_dir / "hierarchical"
    results_dir = study_dir / "results"

    df = pd.read_csv(train_csv)
    X = df.drop(columns=["action"])
    y = df["action"].astype(int)

    print("[train] Final label distribution:", y.value_counts().to_dict())

    X_train, X_test, y_train, y_test = chronological_stratified_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
    )

    # ---------------------------------------------------
    # Create Stage 1 targets
    # ---------------------------------------------------

    y1_train = y_train.map(FINAL_TO_STAGE1).astype(int)
    y1_test = y_test.map(FINAL_TO_STAGE1).astype(int)

    # ---------------------------------------------------
    # Create Stage 2 training/testing sets
    # ---------------------------------------------------

    train_picking_mask = y_train.isin([GOOD_PICKING, BAD_PICKING])
    test_picking_mask = y_test.isin([GOOD_PICKING, BAD_PICKING])

    X2_train = X_train.loc[train_picking_mask]
    y2_train = y_train.loc[train_picking_mask].map(FINAL_TO_STAGE2).astype(int)

    X2_test = X_test.loc[test_picking_mask]
    y2_test = y_test.loc[test_picking_mask].map(FINAL_TO_STAGE2).astype(int)

    results: Dict[str, Dict[str, Any]] = {}

    # ===================================================
    # RANDOM FOREST
    # ===================================================

    if model in ("both", "rf"):

        # ----------------------
        # Stage 1
        # ----------------------

        rf_stage1 = RandomForestClassifier(**RF_PARAMS)

        rf_stage1.fit(X_train, y1_train)

        # ----------------------
        # Stage 2
        # ----------------------

        rf_stage2 = RandomForestClassifier(**RF_PARAMS)

        rf_stage2.fit(X2_train, y2_train)

        # ----------------------
        # Per stage evaluation
        # ----------------------

        stage1_pred = rf_stage1.predict(X_test)

        stage1_result = evaluate_predictions(
            y1_test,
            stage1_pred,
            "stage1",
        )

        stage2_pred = rf_stage2.predict(X2_test)

        stage2_result = evaluate_predictions(
            y2_test,
            stage2_pred,
            "stage2",
        )

        # ----------------------
        # Final end-to-end result
        # ----------------------

        final_pred = _predict_hierarchical(
            rf_stage1,
            rf_stage2,
            X_test,
        )

        combined_result = evaluate_predictions(
            y_test,
            final_pred,
            "flat",
        )

        rf_evaluation = {
            "combined": combined_result,
            "stage1": stage1_result,
            "stage2": stage2_result,
        }

        save_json(
            rf_evaluation,
            results_dir / "hierarchical_rf_results.json",
        )

        save_hierarchical_report(
            rf_evaluation,
            results_dir / "hierarchical_rf_report.md",
            "Standard Hierarchical Architecture - Random Forest",
        )

        # ----------------------
        # Save both models
        # ----------------------

        rf_stage1_path = hierarchical_dir / "rf_stage1.pkl"
        rf_stage2_path = hierarchical_dir / "rf_stage2.pkl"

        with open(rf_stage1_path, "wb") as f:
            pickle.dump(rf_stage1, f)

        with open(rf_stage2_path, "wb") as f:
            pickle.dump(rf_stage2, f)

        # ----------------------

        results["rf"] = {
            "stage1_model": rf_stage1,
            "stage2_model": rf_stage2,
            "evaluation": rf_evaluation,
        }

    # ===================================================
    # XGBOOST
    # ===================================================

    if model in ("both", "xgb"):

        # ----------------------
        # Stage 1
        # ----------------------

        xgb_stage1 = XGBClassifier(**XGB_PARAMS)

        xgb_stage1.fit(X_train, y1_train)

        # ----------------------
        # Stage 2
        # ----------------------

        xgb_stage2 = XGBClassifier(**XGB_PARAMS)

        xgb_stage2.fit(X2_train, y2_train)

        # ----------------------
        # Per stage evaluation
        # ----------------------

        stage1_pred = xgb_stage1.predict(X_test)

        stage1_result = evaluate_predictions(
            y1_test,
            stage1_pred,
            "stage1",
        )

        stage2_pred = xgb_stage2.predict(X2_test)

        stage2_result = evaluate_predictions(
            y2_test,
            stage2_pred,
            "stage2",
        )

        # ----------------------
        # Final end-to-end result
        # ----------------------

        final_pred = _predict_hierarchical(
            xgb_stage1,
            xgb_stage2,
            X_test,
        )

        combined_result = evaluate_predictions(
            y_test,
            final_pred,
            "flat",
        )

        xgb_evaluation = {
            "combined": combined_result,
            "stage1": stage1_result,
            "stage2": stage2_result,
        }

        save_json(
            xgb_evaluation,
            results_dir / "hierarchical_xgb_results.json",
        )

        save_hierarchical_report(
            xgb_evaluation,
            results_dir / "hierarchical_xgb_report.md",
            "Standard Hierarchical Architecture - XGBoost",
        )

        # ----------------------
        # Save both models
        # ----------------------

        xgb_stage1_path = hierarchical_dir / "xgb_stage1.pkl"
        xgb_stage2_path = hierarchical_dir / "xgb_stage2.pkl"

        with open(xgb_stage1_path, "wb") as f:
            pickle.dump(xgb_stage1, f)

        with open(xgb_stage2_path, "wb") as f:
            pickle.dump(xgb_stage2, f)

        results["xgb"] = {
            "stage1_model": xgb_stage1,
            "stage2_model": xgb_stage2,
            "evaluation": xgb_evaluation,
        }

    return results
