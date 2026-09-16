# Hierarchical Architecture With Other - Random Forest

## Combined Performance

**Accuracy:** 0.8475

**Macro F1:** 0.7721

**Weighted F1:** 0.8341

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.7636 | 0.5600 | 0.6462 | 75 |
| Idle | 0.7615 | 0.9706 | 0.8534 | 204 |
| Good Picking | 0.7159 | 0.8750 | 0.7875 | 72 |
| Bad Picking | 0.9333 | 0.4200 | 0.5793 | 100 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 42 | 30 | 2 | 0 | 1 |
| Idle | 2 | 198 | 0 | 3 | 1 |
| Good Picking | 6 | 2 | 63 | 0 | 1 |
| Bad Picking | 5 | 30 | 23 | 42 | 0 |
| Pushing | 0 | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5600 | 0.4000 | 0.0267 | 0.0000 | 0.0133 |
| Idle | 0.0098 | 0.9706 | 0.0000 | 0.0147 | 0.0049 |
| Good Picking | 0.0833 | 0.0278 | 0.8750 | 0.0000 | 0.0139 |
| Bad Picking | 0.0500 | 0.3000 | 0.2300 | 0.4200 | 0.0000 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8863

**Macro F1:** 0.8399

**Weighted F1:** 0.8822

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8511 | 0.5333 | 0.6557 | 75 |
| Idle | 0.7751 | 0.9461 | 0.8521 | 204 |
| Picking | 0.9145 | 0.8081 | 0.8580 | 172 |
| Pushing | 0.9879 | 1.0000 | 0.9939 | 244 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 40 | 30 | 4 | 1 |
| Idle | 1 | 193 | 9 | 1 |
| Picking | 6 | 26 | 139 | 1 |
| Pushing | 0 | 0 | 0 | 244 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.5333 | 0.4000 | 0.0533 | 0.0133 |
| Idle | 0.0049 | 0.9461 | 0.0441 | 0.0049 |
| Picking | 0.0349 | 0.1512 | 0.8081 | 0.0058 |
| Pushing | 0.0000 | 0.0000 | 0.0000 | 1.0000 |

## Stage 2 — Picking Classification

**Accuracy:** 0.8935

**Macro F1:** 0.7740

**Weighted F1:** 0.8824

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.7079 | 0.8750 | 0.7826 | 72 |
| Bad Picking | 0.8800 | 0.4400 | 0.5867 | 100 |
| Other | 0.9245 | 0.9828 | 0.9527 | 523 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 63 | 0 | 9 |
| Bad Picking | 23 | 44 | 33 |
| Other | 3 | 6 | 514 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.8750 | 0.0000 | 0.1250 |
| Bad Picking | 0.2300 | 0.4400 | 0.3300 |
| Other | 0.0057 | 0.0115 | 0.9828 |
