"""Transparent weighted ranking of already-normalized financial factors."""

from math import isfinite


def weighted_score(factors: dict[str, float], weights: dict[str, float]) -> float:
    """Factor scores must be 0..100; positive weights need not sum to 1."""
    if not weights or factors.keys() != weights.keys():
        raise ValueError("factors and weights must have identical nonempty keys")
    if any(not isfinite(v) or v < 0 or v > 100 for v in factors.values()):
        raise ValueError("factor scores must be finite and between 0 and 100")
    if any(not isfinite(v) or v < 0 for v in weights.values()):
        raise ValueError("weights must be finite and nonnegative")
    total = sum(weights.values())
    if total == 0:
        raise ValueError("weights must have a positive sum")
    return sum(factors[key] * weights[key] for key in factors) / total


def rank_companies(companies: dict[str, dict[str, float]],
                   weights: dict[str, float]) -> list[tuple[str, float]]:
    """Return descending scores, deterministic alphabetical tie-break."""
    scores = [(name, weighted_score(factors, weights)) for name, factors in companies.items()]
    return sorted(scores, key=lambda item: (-item[1], item[0]))
