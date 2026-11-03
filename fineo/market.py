"""Illustrative market indicators computed from chronological close prices."""


def simple_moving_average(prices: list[float], window: int) -> list[float | None]:
    if window <= 0:
        raise ValueError("window must be positive")
    if any(price < 0 for price in prices):
        raise ValueError("prices must be nonnegative")
    return [None if i + 1 < window else sum(prices[i + 1 - window:i + 1]) / window
            for i in range(len(prices))]


def rsi(prices: list[float], period: int = 14) -> list[float | None]:
    """Wilder-smoothed RSI; initial RSI at index period."""
    if period < 1:
        raise ValueError("period must be positive")
    if any(p < 0 for p in prices):
        raise ValueError("prices must be nonnegative")
    output: list[float | None] = [None] * len(prices)
    if len(prices) <= period:
        return output
    diffs = [b - a for a, b in zip(prices, prices[1:])]
    avg_gain = sum(max(x, 0) for x in diffs[:period]) / period
    avg_loss = sum(max(-x, 0) for x in diffs[:period]) / period

    def score(gain: float, loss: float) -> float:
        if loss == 0:
            return 50.0 if gain == 0 else 100.0
        return 100 - 100 / (1 + gain / loss)

    output[period] = score(avg_gain, avg_loss)
    for i in range(period + 1, len(prices)):
        gain = max(diffs[i - 1], 0)
        loss = max(-diffs[i - 1], 0)
        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period
        output[i] = score(avg_gain, avg_loss)
    return output
