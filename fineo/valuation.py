"""Simple valuation utilities. All inputs are in consistent currency units."""

from math import isfinite


def _finite(value: float, label: str) -> float:
    result = float(value)
    if not isfinite(result):
        raise ValueError(f"{label} must be finite")
    return result


def pe_implied_equity_value(net_income: float, pe_multiple: float) -> float:
    """Illustrative equity value = earnings attributable to shareholders × P/E."""
    income = _finite(net_income, "net_income")
    multiple = _finite(pe_multiple, "pe_multiple")
    if multiple < 0:
        raise ValueError("pe_multiple cannot be negative")
    return income * multiple


def ev_ebitda_implied_equity_value(ebitda: float, ev_ebitda: float, net_debt: float = 0) -> float:
    """Enterprise value less net debt; assumes no other EV-to-equity adjustments."""
    earnings = _finite(ebitda, "ebitda")
    multiple = _finite(ev_ebitda, "ev_ebitda")
    debt = _finite(net_debt, "net_debt")
    if multiple < 0:
        raise ValueError("ev_ebitda cannot be negative")
    return earnings * multiple - debt


def dcf_equity_value(
    free_cash_flows: list[float],
    discount_rate: float,
    terminal_growth: float,
    net_debt: float = 0,
    mid_year: bool = False,
) -> float:
    """FCFF Gordon-growth DCF. Terminal value at end of final forecast year.

    mid_year applies half-year discounting to explicit FCFF only; terminal
    value is discounted to the final forecast year.
    """
    if not free_cash_flows:
        raise ValueError("free_cash_flows must not be empty")
    flows = [_finite(x, "free_cash_flow") for x in free_cash_flows]
    r = _finite(discount_rate, "discount_rate")
    g = _finite(terminal_growth, "terminal_growth")
    debt = _finite(net_debt, "net_debt")
    if r <= g or r <= -1:
        raise ValueError("discount_rate must exceed terminal_growth and -100%")
    if g <= -1:
        raise ValueError("terminal_growth must exceed -100%")
    pv_flows = sum(cf / (1 + r) ** (year - (0.5 if mid_year else 0))
                   for year, cf in enumerate(flows, start=1))
    tv = flows[-1] * (1 + g) / (r - g)
    return pv_flows + tv / (1 + r) ** len(flows) - debt
