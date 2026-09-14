# Flat Architecture - XGBoost

## Final Performance

**Accuracy:** 0.8567

**Macro F1:** 0.7422

**Weighted F1:** 0.8347

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9286 | 0.6500 | 0.7647 | 20 |
| Idle | 0.9291 | 0.9672 | 0.9478 | 122 |
| Good Picking | 0.5294 | 1.0000 | 0.6923 | 36 |
| Bad Picking | 0.7333 | 0.2115 | 0.3284 | 52 |
| Pushing | 0.9568 | 1.0000 | 0.9779 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 13 | 0 | 4 | 0 | 3 |
| Idle | 0 | 118 | 0 | 4 | 0 |
| Good Picking | 0 | 0 | 36 | 0 | 0 |
| Bad Picking | 1 | 9 | 28 | 11 | 3 |
| Pushing | 0 | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6500 | 0.0000 | 0.2000 | 0.0000 | 0.1500 |
| Idle | 0.0000 | 0.9672 | 0.0000 | 0.0328 | 0.0000 |
| Good Picking | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| Bad Picking | 0.0192 | 0.1731 | 0.5385 | 0.2115 | 0.0577 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
