from typing import Literal, TypeAlias

# =========================
# Preprocessing
# =========================

SENSOR_POSITIONS = ["D_Leg", "D_Wrist"]

# =========================
# Preprocessing
# =========================

BODY_PARTS = [position.lower() for position in SENSOR_POSITIONS]

WIDE_PREFIX_TO_TAG = {
    position.upper(): position.lower() for position in SENSOR_POSITIONS
}

FRAMES_PER_SECOND = 30

ENGINEERED_COLS = [
    "X",
    "Y",
    "Z",
    "XY",
    "YZ",
    "ZX",
    "XYZ",
    "Roll",
    "Pitch",
]

STAT_NAMES = (
    "mean",
    "std",
    "min",
    "max",
    "auc",
    "peaks",
)

# =========================
# Model choices
# =========================

ModelChoice: TypeAlias = Literal["both", "rf", "xgb"]

MODEL_CHOICES = ("both", "rf", "xgb")
DEFAULT_MODEL_CHOICE: ModelChoice = "both"

# =========================
# Final 5-class labels
# =========================

BENDING = 0
IDLE = 1
GOOD_PICKING = 2
BAD_PICKING = 3
PUSHING = 4

FLAT_CLASSES = {
    BENDING: "Bending",
    IDLE: "Idle",
    GOOD_PICKING: "Good Picking",
    BAD_PICKING: "Bad Picking",
    PUSHING: "Pushing",
}


# =========================
# Hierarchical Stage 1
# =========================

S1_BENDING = 0
S1_IDLE = 1
S1_PICKING = 2
S1_PUSHING = 3

STAGE1_CLASSES = {
    S1_BENDING: "Bending",
    S1_IDLE: "Idle",
    S1_PICKING: "Picking",
    S1_PUSHING: "Pushing",
}

FINAL_TO_STAGE1 = {
    BENDING: S1_BENDING,
    IDLE: S1_IDLE,
    GOOD_PICKING: S1_PICKING,
    BAD_PICKING: S1_PICKING,
    PUSHING: S1_PUSHING,
}


# =========================
# Hierarchical Stage 2
# =========================

S2_GOOD = 0
S2_BAD = 1

STAGE2_CLASSES = {
    S2_GOOD: "Good Picking",
    S2_BAD: "Bad Picking",
}

FINAL_TO_STAGE2 = {
    GOOD_PICKING: S2_GOOD,
    BAD_PICKING: S2_BAD,
}

# =========================
# Hierarchical With Other Stage 2
# =========================
OTHER = 2

FINAL_TO_STAGE2_WITH_OTHER = {
    GOOD_PICKING: S2_GOOD,
    BAD_PICKING: S2_BAD,
    BENDING: OTHER,
    IDLE: OTHER,
    PUSHING: OTHER,
}

STAGE2_WITH_OTHER_CLASSES = {
    S2_GOOD: "Good Picking",
    S2_BAD: "Bad Picking",
    OTHER: "Other",
}
# =========================
# Evaluation
# =========================

CLASS_SETS = {
    "flat": FLAT_CLASSES,
    "stage1": STAGE1_CLASSES,
    "stage2": STAGE2_CLASSES,
    "stage2_with_other": STAGE2_WITH_OTHER_CLASSES,
}

# =========================
# Train / test split
# =========================

TEST_SIZE = 0.2
RANDOM_STATE = 42


# =========================
# Random Forest
# =========================

RF_PARAMS = {
    "n_estimators": 400,
    "random_state": RANDOM_STATE,
    "n_jobs": -1,
    "class_weight": "balanced_subsample",
    "max_depth": None,
    "min_samples_leaf": 1,
}


# =========================
# XGBoost
# =========================

XGB_PARAMS = {
    "n_estimators": 300,
    "max_depth": 6,
    "learning_rate": 0.1,
    "subsample": 0.9,
    "colsample_bytree": 0.9,
    "eval_metric": "mlogloss",
    "random_state": RANDOM_STATE,
}

XGB_BINARY_PARAMS = {
    "n_estimators": 300,
    "max_depth": 6,
    "learning_rate": 0.1,
    "subsample": 0.9,
    "colsample_bytree": 0.9,
    "eval_metric": "logloss",
    "random_state": RANDOM_STATE,
}
