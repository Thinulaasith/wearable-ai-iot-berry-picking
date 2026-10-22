# Hierarchical Architecture With Other - Random Forest

## Combined Performance

**Accuracy:** 0.9360

**Macro F1:** 0.9193

**Weighted F1:** 0.9323

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9333 | 0.6462 | 0.7636 | 65 |
| Idle | 0.8644 | 1.0000 | 0.9273 | 102 |
| Good Picking | 0.9785 | 0.9381 | 0.9579 | 97 |
| Bad Picking | 0.9700 | 0.9898 | 0.9798 | 98 |
| Pushing | 0.9453 | 0.9918 | 0.9680 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 42 | 16 | 1 | 1 | 5 |
| Idle | 0 | 102 | 0 | 0 | 0 |
| Good Picking | 2 | 0 | 91 | 2 | 2 |
| Bad Picking | 0 | 0 | 1 | 97 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6462 | 0.2462 | 0.0154 | 0.0154 | 0.0769 |
| Idle | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| Good Picking | 0.0206 | 0.0000 | 0.9381 | 0.0206 | 0.0206 |
| Bad Picking | 0.0000 | 0.0000 | 0.0102 | 0.9898 | 0.0000 |
| Pushing | 0.0082 | 0.0000 | 0.0000 | 0.0000 | 0.9918 |

## Stage 1 — Activity Classification

**Accuracy:** 0.9339

**Macro F1:** 0.8993

**Weighted F1:** 0.9288

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9512 | 0.6000 | 0.7358 | 65 |
| Idle | 0.8621 | 0.9804 | 0.9174 | 102 |
| Picking | 0.9600 | 0.9846 | 0.9722 | 195 |
| Pushing | 0.9528 | 0.9918 | 0.9719 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 39 | 16 | 6 | 4 |
| Idle | 0 | 100 | 2 | 0 |
| Picking | 1 | 0 | 192 | 2 |
| Pushing | 1 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.6000 | 0.2462 | 0.0923 | 0.0615 |
| Idle | 0.0000 | 0.9804 | 0.0196 | 0.0000 |
| Picking | 0.0051 | 0.0000 | 0.9846 | 0.0103 |
| Pushing | 0.0082 | 0.0000 | 0.0000 | 0.9918 |

## Stage 2 — Picking Classification

**Accuracy:** 0.9814

**Macro F1:** 0.9759

**Weighted F1:** 0.9814

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9787 | 0.9485 | 0.9634 | 97 |
| Bad Picking | 0.9604 | 0.9898 | 0.9749 | 98 |
| Other | 0.9896 | 0.9896 | 0.9896 | 289 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 92 | 2 | 3 |
| Bad Picking | 1 | 97 | 0 |
| Other | 1 | 2 | 286 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking | Other |
|---|---:|---:|---:|
| Good Picking | 0.9485 | 0.0206 | 0.0309 |
| Bad Picking | 0.0102 | 0.9898 | 0.0000 |
| Other | 0.0035 | 0.0069 | 0.9896 |
