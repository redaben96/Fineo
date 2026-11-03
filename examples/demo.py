"""Run via: python examples/demo.py (from repository root)."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fineo.valuation import dcf_equity_value, pe_implied_equity_value
from fineo.financial_analysis import ebitda_margin, interest_coverage
from fineo.macro import period_growth
from fineo.market import simple_moving_average, rsi
from fineo.screening import rank_companies
from fineo.document_analysis import extract_metrics

# Completely fabricated figures, not a real security or financial institution.
print("Fineo demo — synthetic data only")
print("DCF equity value:", round(dcf_equity_value([12, 14, 16, 18, 20], 0.10, 0.025, 35), 2))
print("P/E implied value:", pe_implied_equity_value(10, 15))
print("EBITDA margin:", round(ebitda_margin(25, 100) * 100, 1), "%")
print("Interest coverage:", interest_coverage(15, 3))
print("12-month growth:", period_growth([100] * 12 + [105], lag=12)[-1])
prices = [100 + i * 0.8 + (i % 4) for i in range(22)]
print("5-day moving average:", round(simple_moving_average(prices, 5)[-1], 2))
print("RSI (14):", round(rsi(prices, 14)[-1], 2))
scores = {"Company Alpha": {"quality": 80, "value": 60},
          "Company Beta": {"quality": 65, "value": 85}}
print("Ranking:", rank_companies(scores, {"quality": 0.6, "value": 0.4}))
print("Text extraction:", extract_metrics("Revenue: 1,250.50\nEBITDA: 300", ["Revenue", "EBITDA"]))
