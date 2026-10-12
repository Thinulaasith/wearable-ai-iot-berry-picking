# Standard Hierarchical Architecture - XGBoost

## Combined Performance

**Accuracy:** 0.9360

**Macro F1:** 0.9191

**Weighted F1:** 0.9323

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9767 | 0.6462 | 0.7778 | 65 |
| Idle | 0.8632 | 0.9902 | 0.9224 | 102 |
| Good Picking | 0.9381 | 0.9381 | 0.9381 | 97 |
| Bad Picking | 0.9417 | 0.9898 | 0.9652 | 98 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 42 | 16 | 5 | 2 | 0 |
| Idle | 1 | 101 | 0 | 0 | 0 |
| Good Picking | 0 | 0 | 91 | 4 | 2 |
| Bad Picking | 0 | 0 | 1 | 97 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6462 | 0.2462 | 0.0769 | 0.0308 | 0.0000 |
| Idle | 0.0098 | 0.9902 | 0.0000 | 0.0000 | 0.0000 |
| Good Picking | 0.0000 | 0.0000 | 0.9381 | 0.0412 | 0.0206 |
| Bad Picking | 0.0000 | 0.0000 | 0.0102 | 0.9898 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.9463

**Macro F1:** 0.9173

**Weighted F1:** 0.9426

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9767 | 0.6462 | 0.7778 | 65 |
| Idle | 0.8632 | 0.9902 | 0.9224 | 102 |
| Picking | 0.9650 | 0.9897 | 0.9772 | 195 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 42 | 16 | 7 | 0 |
| Idle | 1 | 101 | 0 | 0 |
| Picking | 0 | 0 | 193 | 2 |
| Pushing | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.6462 | 0.2462 | 0.1077 | 0.0000 |
| Idle | 0.0098 | 0.9902 | 0.0000 | 0.0000 |
| Picking | 0.0000 | 0.0000 | 0.9897 | 0.0103 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.9641

**Macro F1:** 0.9641

**Weighted F1:** 0.9641

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9891 | 0.9381 | 0.9630 | 97 |
| Bad Picking | 0.9417 | 0.9898 | 0.9652 | 98 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 91 | 6 |
| Bad Picking | 1 | 97 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.9381 | 0.0619 |
| Bad Picking | 0.0102 | 0.9898 |
