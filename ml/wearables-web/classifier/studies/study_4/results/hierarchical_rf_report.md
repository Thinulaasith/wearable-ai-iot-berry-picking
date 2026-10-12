# Standard Hierarchical Architecture - Random Forest

## Combined Performance

**Accuracy:** 0.7059

**Macro F1:** 0.7111

**Weighted F1:** 0.7006

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8298 | 0.5821 | 0.6842 | 67 |
| Idle | 0.5731 | 0.9608 | 0.7179 | 102 |
| Good Picking | 0.9189 | 0.4533 | 0.6071 | 150 |
| Bad Picking | 0.5281 | 0.6104 | 0.5663 | 154 |
| Pushing | 0.9680 | 0.9918 | 0.9798 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 39 | 15 | 5 | 4 | 4 |
| Idle | 0 | 98 | 0 | 4 | 0 |
| Good Picking | 6 | 0 | 68 | 76 | 0 |
| Bad Picking | 1 | 58 | 1 | 94 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5821 | 0.2239 | 0.0746 | 0.0597 | 0.0597 |
| Idle | 0.0000 | 0.9608 | 0.0000 | 0.0392 | 0.0000 |
| Good Picking | 0.0400 | 0.0000 | 0.4533 | 0.5067 | 0.0000 |
| Bad Picking | 0.0065 | 0.3766 | 0.0065 | 0.6104 | 0.0000 |
| Pushing | 0.0082 | 0.0000 | 0.0000 | 0.0000 | 0.9918 |

## Stage 1 — Activity Classification

**Accuracy:** 0.8353

**Macro F1:** 0.8104

**Weighted F1:** 0.8403

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8298 | 0.5821 | 0.6842 | 67 |
| Idle | 0.5731 | 0.9608 | 0.7179 | 102 |
| Picking | 0.9484 | 0.7862 | 0.8597 | 304 |
| Pushing | 0.9680 | 0.9918 | 0.9798 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 39 | 15 | 9 | 4 |
| Idle | 0 | 98 | 4 | 0 |
| Picking | 7 | 58 | 239 | 0 |
| Pushing | 1 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Picking | Pushing |
|---|---:|---:|---:|---:|
| Bending | 0.5821 | 0.2239 | 0.1343 | 0.0597 |
| Idle | 0.0000 | 0.9608 | 0.0392 | 0.0000 |
| Picking | 0.0230 | 0.1908 | 0.7862 | 0.0000 |
| Pushing | 0.0082 | 0.0000 | 0.0000 | 0.9918 |

## Stage 2 — Picking Classification

**Accuracy:** 0.7270

**Macro F1:** 0.7038

**Weighted F1:** 0.7049

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 0.9855 | 0.4533 | 0.6210 | 150 |
| Bad Picking | 0.6511 | 0.9935 | 0.7866 | 154 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 68 | 82 |
| Bad Picking | 1 | 153 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.4533 | 0.5467 |
| Bad Picking | 0.0065 | 0.9935 |
