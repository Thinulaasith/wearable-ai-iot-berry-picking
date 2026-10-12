# Standard Hierarchical Architecture - Random Forest

## Combined Performance

**Accuracy:** 0.6843

**Macro F1:** 0.6936

**Weighted F1:** 0.6776

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.8387 | 0.5909 | 0.6933 | 44 |
| Idle | 0.5556 | 0.9559 | 0.7027 | 68 |
| Good Picking | 0.9286 | 0.3900 | 0.5493 | 100 |
| Bad Picking | 0.4880 | 0.5922 | 0.5351 | 103 |
| Pushing | 0.9877 | 0.9877 | 0.9877 | 81 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 26 | 10 | 3 | 4 | 1 |
| Idle | 0 | 65 | 0 | 3 | 0 |
| Good Picking | 4 | 0 | 39 | 57 | 0 |
| Bad Picking | 0 | 42 | 0 | 61 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 80 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.5909 | 0.2273 | 0.0682 | 0.0909 | 0.0227 |
| Idle | 0.0000 | 0.9559 | 0.0000 | 0.0441 | 0.0000 |
| Good Picking | 0.0400 | 0.0000 | 0.3900 | 0.5700 | 0.0000 |
| Bad Picking | 0.0000 | 0.4078 | 0.0000 | 0.5922 | 0.0000 |
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

**Accuracy:** 0.7044

**Macro F1:** 0.6729

**Weighted F1:** 0.6744

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Good Picking | 1.0000 | 0.4000 | 0.5714 | 100 |
| Bad Picking | 0.6319 | 1.0000 | 0.7744 | 103 |

### Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 40 | 60 |
| Bad Picking | 0 | 103 |

### Normalized Confusion Matrix

| Actual \ Predicted | Good Picking | Bad Picking |
|---|---:|---:|
| Good Picking | 0.4000 | 0.6000 |
| Bad Picking | 0.0000 | 1.0000 |
