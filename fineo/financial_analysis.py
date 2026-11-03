"""Accounting metrics with explicit denominator checks."""


def safe_ratio(numerator: float, denominator: float) -> float:
    """Return numerator/denominator; fail instead of hiding undefined ratios."""
    if denominator == 0:
        raise ValueError("ratio denominator cannot be zero")
    return numerator / denominator


def ebitda_margin(ebitda: float, revenue: float) -> float:
    return safe_ratio(ebitda, revenue)


def operating_margin(operating_profit: float, revenue: float) -> float:
    return safe_ratio(operating_profit, revenue)


def interest_coverage(operating_profit: float, interest_expense: float) -> float:
    """EBIT/positive gross interest expense."""
    if interest_expense <= 0:
        raise ValueError("interest_expense must be positive")
    return operating_profit / interest_expense


def net_gearing(net_debt: float, equity: float) -> float:
    """Net debt / (net debt + equity); not comparable to debt/equity gearing."""
    return safe_ratio(net_debt, net_debt + equity)


def debt_service_coverage(cash_available_for_debt_service: float, debt_service: float) -> float:
    """CFADS / scheduled interest plus principal cash payments."""
    if debt_service <= 0:
        raise ValueError("debt_service must be positive")
    return cash_available_for_debt_service / debt_service
