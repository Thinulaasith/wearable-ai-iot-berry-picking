# Flat Architecture - XGBoost

## Final Performance

**Accuracy:** 0.6619

**Macro F1:** 0.6841

**Weighted F1:** 0.6571

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9271 | 0.6642 | 0.7739 | 134 |
| Idle | 0.5039 | 0.9608 | 0.6610 | 204 |
| Good Picking | 0.8864 | 0.3887 | 0.5404 | 301 |
| Bad Picking | 0.4381 | 0.4693 | 0.4531 | 309 |
| Pushing | 0.9918 | 0.9918 | 0.9918 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 89 | 32 | 9 | 3 | 1 |
| Idle | 2 | 196 | 0 | 6 | 0 |
| Good Picking | 3 | 3 | 117 | 177 | 1 |
| Bad Picking | 1 | 157 | 6 | 145 | 0 |
| Pushing | 1 | 1 | 0 | 0 | 242 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6642 | 0.2388 | 0.0672 | 0.0224 | 0.0075 |
| Idle | 0.0098 | 0.9608 | 0.0000 | 0.0294 | 0.0000 |
| Good Picking | 0.0100 | 0.0100 | 0.3887 | 0.5880 | 0.0033 |
| Bad Picking | 0.0032 | 0.5081 | 0.0194 | 0.4693 | 0.0000 |
| Pushing | 0.0041 | 0.0041 | 0.0000 | 0.0000 | 0.9918 |
