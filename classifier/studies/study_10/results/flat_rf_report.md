# Flat Architecture - Random Forest

## Final Performance

**Accuracy:** 0.9682

**Macro F1:** 0.9638

**Weighted F1:** 0.9679

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Bending | 0.9792 | 0.8868 | 0.9307 | 53 |
| Idle | 0.9903 | 1.0000 | 0.9951 | 102 |
| Good Picking | 0.9579 | 0.9381 | 0.9479 | 97 |
| Bad Picking | 0.9600 | 0.9796 | 0.9697 | 98 |
| Pushing | 0.9603 | 0.9918 | 0.9758 | 122 |

### Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 47 | 0 | 2 | 0 | 4 |
| Idle | 0 | 102 | 0 | 0 | 0 |
| Good Picking | 0 | 1 | 91 | 4 | 1 |
| Bad Picking | 0 | 0 | 2 | 96 | 0 |
| Pushing | 1 | 0 | 0 | 0 | 121 |

### Normalized Confusion Matrix

| Actual \ Predicted | Bending | Idle | Good Picking | Bad Picking | Pushing |
|---|---:|---:|---:|---:|---:|
| Bending | 0.8868 | 0.0000 | 0.0377 | 0.0000 | 0.0755 |
| Idle | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 |
| Good Picking | 0.0000 | 0.0103 | 0.9381 | 0.0412 | 0.0103 |
| Bad Picking | 0.0000 | 0.0000 | 0.0204 | 0.9796 | 0.0000 |
| Pushing | 0.0082 | 0.0000 | 0.0000 | 0.0000 | 0.9918 |
