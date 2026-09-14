from typing import Literal, TypeAlias

# =========================
# Preprocessing
# =========================

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

BODY_PARTS = [
    "forearm",
    "upper_leg",
    "upper_back",
    "upper_arm",
    "back",
    "left_wrist",
    "right_wrist",
    "wrist",
    "d_leg",
    "d_upper_arm",
    "l_wrist",
    "r_wrist",
]

WIDE_PREFIX_TO_TAG = {
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
    "WRIST": "wrist",
    "D_LEG": "d_leg",
    "D_UPPER_ARM": "d_upper_arm",
    "L_WRIST": "l_wrist",
    "R_WRIST": "r_wrist",
}

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
# Evaluation
# =========================

CLASS_SETS = {
    "flat": FLAT_CLASSES,
    "stage1": STAGE1_CLASSES,
    "stage2": STAGE2_CLASSES,
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
