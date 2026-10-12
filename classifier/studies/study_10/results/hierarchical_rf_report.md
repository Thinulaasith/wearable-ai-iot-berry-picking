# Standard Hierarchical Architecture - Random Forest

## Combined Performance

**Accuracy:** 0.9619

**Macro F1:** 0.9546

**Weighted F1:** 0.9613

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9778 | 0.8302 | 0.8980 | 53 |
| Idle | 1.0000 | 0.9902 | 0.9951 | 102 |
| Good Picking | 0.9479 | 0.9381 | 0.9430 | 97 |
| Bad Picking | 0.9417 | 0.9898 | 0.9652 | 98 |
| Pushing | 0.9528 | 0.9918 | 0.9719 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 44 | 0 | 4 | 0 | 5 |
| Idle | 0 | 101 | 0 | 1 | 0 |
| Good Picking | 0 | 0 | 91 | 5 | 1 |
| Bad Picking | 0 | 0 | 1 | 97 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.8302 | 0.0000 | 0.0755 | 0.0000 | 0.0943 |
| Idle | 0.0000 | 0.9902 | 0.0000 | 0.0098 | 0.0000 |
| Good Picking | 0.0000 | 0.0000 | 0.9381 | 0.0515 | 0.0103 |
| Bad Picking | 0.0000 | 0.0000 | 0.0102 | 0.9898 | 0.0000 |
| Pushing | 0.0082 | 0.0000 | 0.0000 | 0.0000 | 0.9918 |

## Stage 1 — Activity Classification

**Accuracy:** 0.9746

**Macro F1:** 0.9624

**Weighted F1:** 0.9739

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9778 | 0.8302 | 0.8980 | 53 |
| Idle | 1.0000 | 0.9902 | 0.9951 | 102 |
| Picking | 0.9749 | 0.9949 | 0.9848 | 195 |
| Pushing | 0.9528 | 0.9918 | 0.9719 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 44 | 0 | 4 | 5 |
| Idle | 0 | 101 | 1 | 0 |
| Picking | 0 | 0 | 194 | 1 |
| Pushing | 1 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.8302 | 0.0000 | 0.0755 | 0.0943 |
| Idle | 0.0000 | 0.9902 | 0.0098 | 0.0000 |
| Picking | 0.0000 | 0.0000 | 0.9949 | 0.0051 |
| Pushing | 0.0082 | 0.0000 | 0.0000 | 0.9918 |

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
