# Flat Architecture - XGBoost

## Final Performance

**Accuracy:** 0.6869

**Macro F1:** 0.7034

**Weighted F1:** 0.6803

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9062 | 0.6591 | 0.7632 | 44 |
| Idle | 0.5517 | 0.9412 | 0.6957 | 68 |
| Good Picking | 0.9737 | 0.3700 | 0.5362 | 100 |
| Bad Picking | 0.4766 | 0.5922 | 0.5281 | 103 |
| Pushing | 0.9878 | 1.0000 | 0.9939 | 81 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 29 | 10 | 1 | 4 | 0 |
| Idle | 1 | 64 | 0 | 3 | 0 |
| Good Picking | 2 | 0 | 37 | 60 | 1 |
| Bad Picking | 0 | 42 | 0 | 61 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 81 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6591 | 0.2273 | 0.0227 | 0.0909 | 0.0000 |
| Idle | 0.0147 | 0.9412 | 0.0000 | 0.0441 | 0.0000 |
| Good Picking | 0.0200 | 0.0000 | 0.3700 | 0.6000 | 0.0100 |
| Bad Picking | 0.0000 | 0.4078 | 0.0000 | 0.5922 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
