# Flat Architecture - XGBoost

## Final Performance

**Accuracy:** 0.8713

**Macro F1:** 0.7439

**Weighted F1:** 0.8620

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8667 | 0.6842 | 0.7647 | 19 |
| Idle | 0.8603 | 0.9590 | 0.9070 | 122 |
| Good Picking | 0.4286 | 0.7500 | 0.5455 | 12 |
| Bad Picking | 0.7308 | 0.3958 | 0.5135 | 48 |
| Pushing | 0.9779 | 1.0000 | 0.9888 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 13 | 2 | 1 | 1 | 2 |
| Idle | 0 | 117 | 0 | 5 | 0 |
| Good Picking | 0 | 2 | 9 | 1 | 0 |
| Bad Picking | 2 | 15 | 11 | 19 | 1 |
| Pushing | 0 | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6842 | 0.1053 | 0.0526 | 0.0526 | 0.1053 |
| Idle | 0.0000 | 0.9590 | 0.0000 | 0.0410 | 0.0000 |
| Good Picking | 0.0000 | 0.1667 | 0.7500 | 0.0833 | 0.0000 |
| Bad Picking | 0.0417 | 0.3125 | 0.2292 | 0.3958 | 0.0208 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
