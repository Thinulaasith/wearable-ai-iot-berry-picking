# Flat Architecture - XGBoost

## Final Performance

**Accuracy:** 0.9746

**Macro F1:** 0.9704

**Weighted F1:** 0.9744

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9608 | 0.9245 | 0.9423 | 53 |
| Idle | 0.9902 | 0.9902 | 0.9902 | 102 |
| Good Picking | 0.9579 | 0.9381 | 0.9479 | 97 |
| Bad Picking | 0.9700 | 0.9898 | 0.9798 | 98 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 49 | 1 | 3 | 0 | 0 |
| Idle | 1 | 101 | 0 | 0 | 0 |
| Good Picking | 1 | 0 | 91 | 3 | 2 |
| Bad Picking | 0 | 0 | 1 | 97 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.9245 | 0.0189 | 0.0566 | 0.0000 | 0.0000 |
| Idle | 0.0098 | 0.9902 | 0.0000 | 0.0000 | 0.0000 |
| Good Picking | 0.0103 | 0.0000 | 0.9381 | 0.0309 | 0.0206 |
| Bad Picking | 0.0000 | 0.0000 | 0.0102 | 0.9898 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
