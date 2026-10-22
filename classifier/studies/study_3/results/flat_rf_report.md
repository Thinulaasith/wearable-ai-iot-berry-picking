# Flat Architecture - Random Forest

## Final Performance

**Accuracy:** 0.8475

**Macro F1:** 0.7741

**Weighted F1:** 0.8358

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8000 | 0.5333 | 0.6400 | 75 |
| Idle | 0.7717 | 0.9608 | 0.8559 | 204 |
| Good Picking | 0.7033 | 0.8889 | 0.7853 | 72 |
| Bad Picking | 0.8519 | 0.4600 | 0.5974 | 100 |
| Pushing | 0.9878 | 0.9959 | 0.9918 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 40 | 30 | 3 | 1 | 1 |
| Idle | 1 | 196 | 0 | 6 | 1 |
| Good Picking | 6 | 0 | 64 | 1 | 1 |
| Bad Picking | 3 | 27 | 24 | 46 | 0 |
| Pushing | 0 | 1 | 0 | 0 | 243 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5333 | 0.4000 | 0.0400 | 0.0133 | 0.0133 |
| Idle | 0.0049 | 0.9608 | 0.0000 | 0.0294 | 0.0049 |
| Good Picking | 0.0833 | 0.0000 | 0.8889 | 0.0139 | 0.0139 |
| Bad Picking | 0.0300 | 0.2700 | 0.2400 | 0.4600 | 0.0000 |
| Pushing | 0.0000 | 0.0041 | 0.0000 | 0.0000 | 0.9959 |
