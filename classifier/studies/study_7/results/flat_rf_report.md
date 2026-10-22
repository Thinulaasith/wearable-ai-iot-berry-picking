# Flat Architecture - Random Forest

## Final Performance

**Accuracy:** 0.8559

**Macro F1:** 0.7830

**Weighted F1:** 0.8462

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.7037 | 0.5135 | 0.5938 | 37 |
| Idle | 0.7903 | 0.9608 | 0.8673 | 102 |
| Good Picking | 0.7273 | 0.8889 | 0.8000 | 36 |
| Bad Picking | 0.8966 | 0.5200 | 0.6582 | 50 |
| Pushing | 0.9919 | 1.0000 | 0.9959 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 19 | 15 | 2 | 0 | 1 |
| Idle | 1 | 98 | 0 | 3 | 0 |
| Good Picking | 4 | 0 | 32 | 0 | 0 |
| Bad Picking | 3 | 11 | 10 | 26 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5135 | 0.4054 | 0.0541 | 0.0000 | 0.0270 |
| Idle | 0.0098 | 0.9608 | 0.0000 | 0.0294 | 0.0000 |
| Good Picking | 0.1111 | 0.0000 | 0.8889 | 0.0000 | 0.0000 |
| Bad Picking | 0.0600 | 0.2200 | 0.2000 | 0.5200 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
