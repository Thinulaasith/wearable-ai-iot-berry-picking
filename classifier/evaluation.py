import json
from pathlib import Path
from typing import Any, Dict

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

from config import (
    CLASS_SETS,
)


def evaluate_predictions(
    y_true,
    y_pred,
    class_set: str,
) -> Dict[str, Any]:

    if class_set not in CLASS_SETS:
        raise ValueError(f"Unknown class set: {class_set}")

    class_names = CLASS_SETS[class_set]

    labels = list(class_names.keys())
    names = list(class_names.values())

    report = classification_report(
        y_true,
        y_pred,
        labels=labels,
        target_names=names,
        output_dict=True,
        zero_division=0,
    )

    cm = confusion_matrix(
        y_true,
        y_pred,
        labels=labels,
    )

    normalized_cm = confusion_matrix(
        y_true,
        y_pred,
        labels=labels,
        normalize="true",
    )

    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_f1": float(report["macro avg"]["f1-score"]),
        "weighted_f1": float(report["weighted avg"]["f1-score"]),
        "class_names": names,
        "classification_report": report,
        "confusion_matrix": cm.tolist(),
        "normalized_confusion_matrix": normalized_cm.tolist(),
    }


def save_json(
    results: Dict[str, Any],
    path: Path,
) -> None:
    """
    Save results in machine-readable JSON format.
    """

    with open(path, "w") as f:
        json.dump(results, f, indent=4)


def _result_to_markdown(
    title: str,
    result: Dict[str, Any],
) -> str:
    """
    Convert one evaluation result into Markdown.
    Used internally by both flat and hierarchical reports.
    """

    lines = []

    lines.append(f"## {title}")
    lines.append("")
    lines.append(f"**Accuracy:** {result['accuracy']:.4f}")
    lines.append("")
    lines.append(f"**Macro F1:** {result['macro_f1']:.4f}")
    lines.append("")
    lines.append(f"**Weighted F1:** {result['weighted_f1']:.4f}")
    lines.append("")

    # -----------------------------
    # Classification report
    # -----------------------------

    lines.append("### Classification Report")
    lines.append("")
    lines.append("| Class | Precision | Recall | F1-score | Support |")
    lines.append("|---|---:|---:|---:|---:|")

    report = result["classification_report"]

    for class_name in result["class_names"]:
        values = report[class_name]

        lines.append(
            f"| {class_name} "
            f"| {values['precision']:.4f} "
            f"| {values['recall']:.4f} "
            f"| {values['f1-score']:.4f} "
            f"| {int(values['support'])} |"
        )

    # -----------------------------
    # Confusion matrix
    # -----------------------------

    lines.append("")
    lines.append("### Confusion Matrix")
    lines.append("")

    names = result["class_names"]
    matrix = result["confusion_matrix"]

    lines.append("| Actual \\ Predicted | " + " | ".join(names) + " |")

    lines.append("|---|" + "---:|" * len(names))

    for name, row in zip(names, matrix):
        lines.append(f"| {name} | " + " | ".join(str(value) for value in row) + " |")

    # -----------------------------
    # Normalized confusion matrix
    # -----------------------------

    lines.append("")
    lines.append("### Normalized Confusion Matrix")
    lines.append("")

    normalized = result["normalized_confusion_matrix"]

    lines.append("| Actual \\ Predicted | " + " | ".join(names) + " |")

    lines.append("|---|" + "---:|" * len(names))

    for name, row in zip(names, normalized):
        lines.append(
            f"| {name} | " + " | ".join(f"{value:.4f}" for value in row) + " |"
        )

    lines.append("")

    return "\n".join(lines)


def save_flat_report(
    result: Dict[str, Any],
    path: Path,
    title: str,
) -> None:
    """
    Save a human-readable report for a flat model.
    """

    markdown = f"# {title}\n\n"
    markdown += _result_to_markdown("Final Performance", result)

    with open(path, "w") as f:
        f.write(markdown)


def save_hierarchical_report(
    results: Dict[str, Any],
    path: Path,
    title: str,
) -> None:
    """
    Save a human-readable report for a hierarchical model.
    """

    markdown = f"# {title}\n\n"

    markdown += _result_to_markdown(
        "Combined Performance",
        results["combined"],
    )

    markdown += "\n"

    markdown += _result_to_markdown(
        "Stage 1 — Activity Classification",
        results["stage1"],
    )

    markdown += "\n"

    markdown += _result_to_markdown(
        "Stage 2 — Picking Classification",
        results["stage2"],
    )

    with open(path, "w") as f:
        f.write(markdown)
