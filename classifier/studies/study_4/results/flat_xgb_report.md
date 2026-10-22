# Flat Architecture - XGBoost

## Final Performance

**Accuracy:** 0.6672

**Macro F1:** 0.6922

**Weighted F1:** 0.6652

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9583 | 0.6866 | 0.8000 | 67 |
| Idle | 0.4948 | 0.9314 | 0.6463 | 102 |
| Good Picking | 0.9524 | 0.4000 | 0.5634 | 150 |
| Bad Picking | 0.4405 | 0.4805 | 0.4596 | 154 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 46 | 16 | 3 | 2 | 0 |
| Idle | 0 | 95 | 0 | 7 | 0 |
| Good Picking | 1 | 2 | 60 | 85 | 2 |
| Bad Picking | 1 | 79 | 0 | 74 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6866 | 0.2388 | 0.0448 | 0.0299 | 0.0000 |
| Idle | 0.0000 | 0.9314 | 0.0000 | 0.0686 | 0.0000 |
| Good Picking | 0.0067 | 0.0133 | 0.4000 | 0.5667 | 0.0133 |
| Bad Picking | 0.0065 | 0.5130 | 0.0000 | 0.4805 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
