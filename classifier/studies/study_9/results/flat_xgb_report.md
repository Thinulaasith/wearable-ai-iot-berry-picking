# Flat Architecture - XGBoost

## Final Performance

**Accuracy:** 0.9401

**Macro F1:** 0.9262

**Weighted F1:** 0.9378

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9574 | 0.6923 | 0.8036 | 65 |
| Idle | 0.8559 | 0.9902 | 0.9182 | 102 |
| Good Picking | 0.9479 | 0.9381 | 0.9430 | 97 |
| Bad Picking | 0.9697 | 0.9796 | 0.9746 | 98 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 45 | 16 | 3 | 1 | 0 |
| Idle | 1 | 101 | 0 | 0 | 0 |
| Good Picking | 1 | 1 | 91 | 2 | 2 |
| Bad Picking | 0 | 0 | 2 | 96 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6923 | 0.2462 | 0.0462 | 0.0154 | 0.0000 |
| Idle | 0.0098 | 0.9902 | 0.0000 | 0.0000 | 0.0000 |
| Good Picking | 0.0103 | 0.0103 | 0.9381 | 0.0206 | 0.0206 |
| Bad Picking | 0.0000 | 0.0000 | 0.0204 | 0.9796 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
