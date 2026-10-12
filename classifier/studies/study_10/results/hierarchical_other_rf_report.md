# Hierarchical Architecture With Other - Random Forest

## Combined Performance

**Accuracy:** 0.9682

**Macro F1:** 0.9626

**Weighted F1:** 0.9679

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9583 | 0.8679 | 0.9109 | 53 |
| Idle | 0.9903 | 1.0000 | 0.9951 | 102 |
| Good Picking | 0.9891 | 0.9381 | 0.9630 | 97 |
| Bad Picking | 0.9700 | 0.9898 | 0.9798 | 98 |
| Pushing | 0.9380 | 0.9918 | 0.9641 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 46 | 0 | 0 | 0 | 7 |
| Idle | 0 | 102 | 0 | 0 | 0 |
| Good Picking | 1 | 1 | 91 | 3 | 1 |
| Bad Picking | 0 | 0 | 1 | 97 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.8679 | 0.0000 | 0.0000 | 0.0000 | 0.1321 |
| Idle | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| Good Picking | 0.0103 | 0.0103 | 0.9381 | 0.0309 | 0.0103 |
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

**Accuracy:** 0.9852

**Macro F1:** 0.9791

**Weighted F1:** 0.9850

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9891 | 0.9381 | 0.9630 | 97 |
| Bad Picking | 0.9700 | 0.9898 | 0.9798 | 98 |
| Other | 0.9893 | 1.0000 | 0.9946 | 277 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 91 | 3 | 3 |
| Bad Picking | 1 | 97 | 0 |
| Other | 0 | 0 | 277 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.9381 | 0.0309 | 0.0309 |
| Bad Picking | 0.0102 | 0.9898 | 0.0000 |
| Other | 0.0000 | 0.0000 | 1.0000 |
