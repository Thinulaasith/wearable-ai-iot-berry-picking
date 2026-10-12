# Flat Architecture - Random Forest

## Final Performance

**Accuracy:** 0.6843

**Macro F1:** 0.6955

**Weighted F1:** 0.6778

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8438 | 0.6136 | 0.7105 | 44 |
| Idle | 0.5508 | 0.9559 | 0.6989 | 68 |
| Good Picking | 0.9286 | 0.3900 | 0.5493 | 100 |
| Bad Picking | 0.4878 | 0.5825 | 0.5310 | 103 |
| Pushing | 0.9877 | 0.9877 | 0.9877 | 81 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 27 | 10 | 3 | 3 | 1 |
| Idle | 0 | 65 | 0 | 3 | 0 |
| Good Picking | 4 | 0 | 39 | 57 | 0 |
| Bad Picking | 0 | 43 | 0 | 60 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 80 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6136 | 0.2273 | 0.0682 | 0.0682 | 0.0227 |
| Idle | 0.0000 | 0.9559 | 0.0000 | 0.0441 | 0.0000 |
| Good Picking | 0.0400 | 0.0000 | 0.3900 | 0.5700 | 0.0000 |
| Bad Picking | 0.0000 | 0.4175 | 0.0000 | 0.5825 | 0.0000 |
| Pushing | 0.0123 | 0.0000 | 0.0000 | 0.0000 | 0.9877 |
