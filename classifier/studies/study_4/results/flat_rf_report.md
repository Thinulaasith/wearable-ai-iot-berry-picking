# Flat Architecture - Random Forest

## Final Performance

**Accuracy:** 0.6975

**Macro F1:** 0.7113

**Weighted F1:** 0.6929

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8214 | 0.6866 | 0.7480 | 67 |
| Idle | 0.5475 | 0.9608 | 0.6975 | 102 |
| Good Picking | 0.9844 | 0.4200 | 0.5888 | 150 |
| Bad Picking | 0.5000 | 0.5649 | 0.5305 | 154 |
| Pushing | 0.9918 | 0.9918 | 0.9918 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 46 | 16 | 1 | 3 | 1 |
| Idle | 1 | 98 | 0 | 3 | 0 |
| Good Picking | 6 | 0 | 63 | 81 | 0 |
| Bad Picking | 2 | 65 | 0 | 87 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6866 | 0.2388 | 0.0149 | 0.0448 | 0.0149 |
| Idle | 0.0098 | 0.9608 | 0.0000 | 0.0294 | 0.0000 |
| Good Picking | 0.0400 | 0.0000 | 0.4200 | 0.5400 | 0.0000 |
| Bad Picking | 0.0130 | 0.4221 | 0.0000 | 0.5649 | 0.0000 |
| Pushing | 0.0082 | 0.0000 | 0.0000 | 0.0000 | 0.9918 |
