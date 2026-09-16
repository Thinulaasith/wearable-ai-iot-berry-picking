# Flat Architecture - XGBoost

## Final Performance

**Accuracy:** 0.8374

**Macro F1:** 0.7660

**Weighted F1:** 0.8261

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8571 | 0.5600 | 0.6774 | 75 |
| Idle | 0.7570 | 0.9314 | 0.8352 | 204 |
| Good Picking | 0.7079 | 0.8750 | 0.7826 | 72 |
| Bad Picking | 0.7288 | 0.4300 | 0.5409 | 100 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 42 | 30 | 2 | 1 | 0 |
| Idle | 1 | 190 | 0 | 13 | 0 |
| Good Picking | 3 | 1 | 63 | 2 | 3 |
| Bad Picking | 3 | 30 | 24 | 43 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5600 | 0.4000 | 0.0267 | 0.0133 | 0.0000 |
| Idle | 0.0049 | 0.9314 | 0.0000 | 0.0637 | 0.0000 |
| Good Picking | 0.0417 | 0.0139 | 0.8750 | 0.0278 | 0.0417 |
| Bad Picking | 0.0300 | 0.3000 | 0.2400 | 0.4300 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
