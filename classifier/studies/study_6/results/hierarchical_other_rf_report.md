# Hierarchical Architecture With Other - Random Forest

## Combined Performance

**Accuracy:** 0.6692

**Macro F1:** 0.6803

**Weighted F1:** 0.6622

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8387 | 0.5909 | 0.6933 | 44 |
| Idle | 0.5152 | 1.0000 | 0.6800 | 68 |
| Good Picking | 0.9302 | 0.4000 | 0.5594 | 100 |
| Bad Picking | 0.4679 | 0.4951 | 0.4811 | 103 |
| Pushing | 0.9877 | 0.9877 | 0.9877 | 81 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 26 | 11 | 3 | 3 | 1 |
| Idle | 0 | 68 | 0 | 0 | 0 |
| Good Picking | 4 | 1 | 40 | 55 | 0 |
| Bad Picking | 0 | 52 | 0 | 51 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 80 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5909 | 0.2500 | 0.0682 | 0.0682 | 0.0227 |
| Idle | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| Good Picking | 0.0400 | 0.0100 | 0.4000 | 0.5500 | 0.0000 |
| Bad Picking | 0.0000 | 0.5049 | 0.0000 | 0.4951 | 0.0000 |
| Pushing | 0.0123 | 0.0000 | 0.0000 | 0.0000 | 0.9877 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8283

**Macro F1:** 0.8081

**Weighted F1:** 0.8348

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8387 | 0.5909 | 0.6933 | 44 |
| Idle | 0.5556 | 0.9559 | 0.7027 | 68 |
| Picking | 0.9401 | 0.7734 | 0.8486 | 203 |
| Pushing | 0.9877 | 0.9877 | 0.9877 | 81 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 26 | 10 | 7 | 1 |
| Idle | 0 | 65 | 3 | 0 |
| Picking | 4 | 42 | 157 | 0 |
| Pushing | 1 | 0 | 0 | 80 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.5909 | 0.2273 | 0.1591 | 0.0227 |
| Idle | 0.0000 | 0.9559 | 0.0441 | 0.0000 |
| Picking | 0.0197 | 0.2069 | 0.7734 | 0.0000 |
| Pushing | 0.0123 | 0.0000 | 0.0000 | 0.9877 |

## Stage 2 — Picking Classification

**Accuracy:** 0.7045

**Macro F1:** 0.6365

**Weighted F1:** 0.6873

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9302 | 0.4000 | 0.5594 | 100 |
| Bad Picking | 0.4732 | 0.5146 | 0.4930 | 103 |
| Other | 0.7718 | 0.9637 | 0.8571 | 193 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 40 | 55 | 5 |
| Bad Picking | 0 | 53 | 50 |
| Other | 3 | 4 | 186 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.4000 | 0.5500 | 0.0500 |
| Bad Picking | 0.0000 | 0.5146 | 0.4854 |
| Other | 0.0155 | 0.0207 | 0.9637 |
