# Flat Architecture - XGBoost

## Final Performance

**Accuracy:** 0.8646

**Macro F1:** 0.8129

**Weighted F1:** 0.8586

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8696 | 0.5405 | 0.6667 | 37 |
| Idle | 0.7881 | 0.9118 | 0.8455 | 102 |
| Good Picking | 0.8049 | 0.9167 | 0.8571 | 36 |
| Bad Picking | 0.7805 | 0.6400 | 0.7033 | 50 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 20 | 14 | 2 | 1 | 0 |
| Idle | 1 | 93 | 0 | 8 | 0 |
| Good Picking | 1 | 0 | 33 | 0 | 2 |
| Bad Picking | 1 | 11 | 6 | 32 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5405 | 0.3784 | 0.0541 | 0.0270 | 0.0000 |
| Idle | 0.0098 | 0.9118 | 0.0000 | 0.0784 | 0.0000 |
| Good Picking | 0.0278 | 0.0000 | 0.9167 | 0.0000 | 0.0556 |
| Bad Picking | 0.0200 | 0.2200 | 0.1200 | 0.6400 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
