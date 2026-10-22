# Standard Hierarchical Architecture - Random Forest

## Combined Performance

**Accuracy:** 0.9236

**Macro F1:** 0.9037

**Weighted F1:** 0.9185

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9512 | 0.6000 | 0.7358 | 65 |
| Idle | 0.8621 | 0.9804 | 0.9174 | 102 |
| Good Picking | 0.9474 | 0.9278 | 0.9375 | 97 |
| Bad Picking | 0.9238 | 0.9898 | 0.9557 | 98 |
| Pushing | 0.9528 | 0.9918 | 0.9719 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 39 | 16 | 4 | 2 | 4 |
| Idle | 0 | 100 | 0 | 2 | 0 |
| Good Picking | 1 | 0 | 90 | 4 | 2 |
| Bad Picking | 0 | 0 | 1 | 97 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.6000 | 0.2462 | 0.0615 | 0.0308 | 0.0615 |
| Idle | 0.0000 | 0.9804 | 0.0000 | 0.0196 | 0.0000 |
| Good Picking | 0.0103 | 0.0000 | 0.9278 | 0.0412 | 0.0206 |
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
