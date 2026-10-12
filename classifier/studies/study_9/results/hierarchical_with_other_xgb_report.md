# Hierarchical Architecture With Other - XGBoost

## Combined Performance

**Accuracy:** 0.9421

**Macro F1:** 0.9293

**Weighted F1:** 0.9402

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9583 | 0.7077 | 0.8142 | 65 |
| Idle | 0.8559 | 0.9902 | 0.9182 | 102 |
| Good Picking | 0.9579 | 0.9381 | 0.9479 | 97 |
| Bad Picking | 0.9697 | 0.9796 | 0.9746 | 98 |
| Pushing | 0.9839 | 1.0000 | 0.9919 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 46 | 17 | 2 | 0 | 0 |
| Idle | 1 | 101 | 0 | 0 | 0 |
| Good Picking | 1 | 0 | 91 | 3 | 2 |
| Bad Picking | 0 | 0 | 2 | 96 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 122 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.7077 | 0.2615 | 0.0308 | 0.0000 | 0.0000 |
| Idle | 0.0098 | 0.9902 | 0.0000 | 0.0000 | 0.0000 |
| Good Picking | 0.0103 | 0.0000 | 0.9381 | 0.0309 | 0.0206 |
| Bad Picking | 0.0000 | 0.0000 | 0.0204 | 0.9796 | 0.0000 |
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

**Accuracy:** 0.9793

**Macro F1:** 0.9713

**Weighted F1:** 0.9793

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9579 | 0.9381 | 0.9479 | 97 |
| Bad Picking | 0.9697 | 0.9796 | 0.9746 | 98 |
| Other | 0.9897 | 0.9931 | 0.9914 | 289 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 91 | 3 | 3 |
| Bad Picking | 2 | 96 | 0 |
| Other | 2 | 0 | 287 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.9381 | 0.0309 | 0.0309 |
| Bad Picking | 0.0204 | 0.9796 | 0.0000 |
| Other | 0.0069 | 0.0000 | 0.9931 |
