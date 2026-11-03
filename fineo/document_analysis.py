"""Rule-based extraction from plain-text statements, not PDF or AI inference."""

import re


def extract_labeled_number(text: str, label: str) -> float | None:
    """Extract first number following an exact label on a line.

    Accepts thousands separators as commas and decimal points as dots.
    Examples: 'Revenue: 1,250.50' and 'EBITDA 250'.
    Does not support all international number conventions.
    """
    expression = re.compile(
        rf"(?im)^\s*{re.escape(label)}\s*[:=]?\s*"
        r"([-+]?\d{1,3}(?:,\d{3})*(?:\.\d+)?|[-+]?\d+(?:\.\d+)?)\s*$"
    )
    match = expression.search(text)
    return float(match.group(1).replace(",", "")) if match else None


def extract_metrics(text: str, labels: list[str]) -> dict[str, float | None]:
    return {label: extract_labeled_number(text, label) for label in labels}
