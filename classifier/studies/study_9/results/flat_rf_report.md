# Flat Architecture - Random Forest

## Final Performance

**Accuracy:** 0.9256

**Macro F1:** 0.9051

**Weighted F1:** 0.9206

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9286 | 0.6000 | 0.7290 | 65 |
| Idle | 0.8644 | 1.0000 | 0.9273 | 102 |
| Good Picking | 0.9474 | 0.9278 | 0.9375 | 97 |
| Bad Picking | 0.9412 | 0.9796 | 0.9600 | 98 |
| Pushing | 0.9528 | 0.9918 | 0.9719 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 39 | 16 | 3 | 3 | 4 |
| Idle | 0 | 102 | 0 | 0 | 0 |
| Good Picking | 2 | 0 | 90 | 3 | 2 |
| Bad Picking | 0 | 0 | 2 | 96 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6000 | 0.2462 | 0.0462 | 0.0462 | 0.0615 |
| Idle | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| Good Picking | 0.0206 | 0.0000 | 0.9278 | 0.0309 | 0.0206 |
| Bad Picking | 0.0000 | 0.0000 | 0.0204 | 0.9796 | 0.0000 |
| Pushing | 0.0082 | 0.0000 | 0.0000 | 0.0000 | 0.9918 |
