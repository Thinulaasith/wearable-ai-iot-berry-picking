# Standard Hierarchical Architecture - XGBoost

## Combined Performance

**Accuracy:** 0.9767

**Macro F1:** 0.9743

**Weighted F1:** 0.9766

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9804 | 0.9434 | 0.9615 | 53 |
| Idle | 1.0000 | 0.9902 | 0.9951 | 102 |
| Good Picking | 0.9579 | 0.9381 | 0.9479 | 97 |
| Bad Picking | 0.9604 | 0.9898 | 0.9749 | 98 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 50 | 0 | 3 | 0 | 0 |
| Idle | 1 | 101 | 0 | 0 | 0 |
| Good Picking | 0 | 0 | 91 | 4 | 2 |
| Bad Picking | 0 | 0 | 1 | 97 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.9434 | 0.0000 | 0.0566 | 0.0000 | 0.0000 |
| Idle | 0.0098 | 0.9902 | 0.0000 | 0.0000 | 0.0000 |
| Good Picking | 0.0000 | 0.0000 | 0.9381 | 0.0412 | 0.0206 |
| Bad Picking | 0.0000 | 0.0000 | 0.0102 | 0.9898 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.9873

**Macro F1:** 0.9839

**Weighted F1:** 0.9872

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9804 | 0.9434 | 0.9615 | 53 |
| Idle | 1.0000 | 0.9902 | 0.9951 | 102 |
| Picking | 0.9847 | 0.9897 | 0.9872 | 195 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 50 | 0 | 3 | 0 |
| Idle | 1 | 101 | 0 | 0 |
| Picking | 0 | 0 | 193 | 2 |
| Pushing | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.9434 | 0.0000 | 0.0566 | 0.0000 |
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
