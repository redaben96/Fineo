"""Simple economic time-series transformations; data order is chronological."""


def percentage_change(previous: float, current: float) -> float:
    """Return decimal growth rate (0.05 means +5%)."""
    if previous == 0:
        raise ValueError("previous observation cannot be zero")
    return current / previous - 1


def period_growth(values: list[float], lag: int = 1) -> list[float | None]:
    """Leading lag observations become None; lag=12 for monthly YoY."""
    if lag < 1:
        raise ValueError("lag must be >= 1")
    return [None if i < lag else percentage_change(values[i - lag], values[i])
            for i in range(len(values))]


def rebase(values: list[float], base: float = 100.0) -> list[float]:
    """Rebase an ordered series relative to its first observation."""
    if not values:
        return []
    if values[0] == 0:
        raise ValueError("first observation cannot be zero")
    return [base * v / values[0] for v in values]
