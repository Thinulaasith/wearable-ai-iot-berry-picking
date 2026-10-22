# Flat Architecture - XGBoost

## Final Performance

**Accuracy:** 0.8518

**Macro F1:** 0.7867

**Weighted F1:** 0.8430

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8400 | 0.5600 | 0.6720 | 75 |
| Idle | 0.7742 | 0.9412 | 0.8496 | 204 |
| Good Picking | 0.7241 | 0.8750 | 0.7925 | 72 |
| Bad Picking | 0.8095 | 0.5100 | 0.6258 | 100 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 42 | 31 | 2 | 0 | 0 |
| Idle | 2 | 192 | 0 | 10 | 0 |
| Good Picking | 3 | 1 | 63 | 2 | 3 |
| Bad Picking | 3 | 24 | 22 | 51 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5600 | 0.4133 | 0.0267 | 0.0000 | 0.0000 |
| Idle | 0.0098 | 0.9412 | 0.0000 | 0.0490 | 0.0000 |
| Good Picking | 0.0417 | 0.0139 | 0.8750 | 0.0278 | 0.0417 |
| Bad Picking | 0.0300 | 0.2400 | 0.2200 | 0.5100 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
