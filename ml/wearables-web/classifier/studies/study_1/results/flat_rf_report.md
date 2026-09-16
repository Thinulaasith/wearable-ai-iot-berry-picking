# Flat Architecture - Random Forest

## Final Performance

**Accuracy:** 0.8862

**Macro F1:** 0.7680

**Weighted F1:** 0.8779

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.7500 | 0.7895 | 0.7692 | 19 |
| Idle | 0.8939 | 0.9672 | 0.9291 | 122 |
| Good Picking | 0.5000 | 0.7500 | 0.6000 | 12 |
| Bad Picking | 0.7500 | 0.4375 | 0.5526 | 48 |
| Pushing | 0.9779 | 1.0000 | 0.9888 | 133 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 15 | 2 | 0 | 0 | 2 |
| Idle | 0 | 118 | 0 | 4 | 0 |
| Good Picking | 0 | 0 | 9 | 3 | 0 |
| Bad Picking | 5 | 12 | 9 | 21 | 1 |
| Pushing | 0 | 0 | 0 | 0 | 133 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.7895 | 0.1053 | 0.0000 | 0.0000 | 0.1053 |
| Idle | 0.0000 | 0.9672 | 0.0000 | 0.0328 | 0.0000 |
| Good Picking | 0.0000 | 0.0000 | 0.7500 | 0.2500 | 0.0000 |
| Bad Picking | 0.1042 | 0.2500 | 0.1875 | 0.4375 | 0.0208 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
