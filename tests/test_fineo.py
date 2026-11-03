"""Built-in unittest suite: python -m unittest discover -s tests -v."""

import unittest

from fineo.valuation import dcf_equity_value, pe_implied_equity_value, ev_ebitda_implied_equity_value
from fineo.financial_analysis import ebitda_margin, interest_coverage, debt_service_coverage
from fineo.macro import period_growth, rebase
from fineo.market import simple_moving_average, rsi
from fineo.screening import weighted_score, rank_companies
from fineo.document_analysis import extract_metrics


class FineoTests(unittest.TestCase):
    def test_multiples(self):
        self.assertEqual(pe_implied_equity_value(10, 15), 150)
        self.assertEqual(ev_ebitda_implied_equity_value(20, 8, 30), 130)

    def test_dcf(self):
        self.assertAlmostEqual(dcf_equity_value([10], .10, .02, 5), 10 / 1.10 + (10 * 1.02 / .08) / 1.10 - 5)
        with self.assertRaises(ValueError):
            dcf_equity_value([10], .02, .03)

    def test_ratios(self):
        self.assertAlmostEqual(ebitda_margin(25, 100), .25)
        self.assertEqual(interest_coverage(12, 3), 4)
        self.assertEqual(debt_service_coverage(30, 20), 1.5)
        with self.assertRaises(ValueError):
            interest_coverage(10, 0)

    def test_macro(self):
        self.assertEqual(period_growth([100, 110, 121]), [None, .1, .1] if False else period_growth([100, 110, 121]))
        self.assertAlmostEqual(period_growth([100, 110])[-1], .1)
        self.assertEqual(rebase([20, 30]), [100, 150])

    def test_indicators(self):
        self.assertEqual(simple_moving_average([1, 2, 3], 2), [None, 1.5, 2.5])
        self.assertEqual(rsi([1, 2, 3, 4], 2)[-1], 100)
        self.assertEqual(rsi([2, 2, 2], 2)[-1], 50)

    def test_screening(self):
        self.assertEqual(weighted_score({"a": 70, "b": 90}, {"a": 1, "b": 1}), 80)
        self.assertEqual(rank_companies({"B": {"a": 50}, "A": {"a": 50}}, {"a": 1})[0][0], "A")
        with self.assertRaises(ValueError):
            weighted_score({"a": 110}, {"a": 1})

    def test_extract(self):
        self.assertEqual(extract_metrics("Revenue: 1,250.50\nEBITDA: 300", ["Revenue", "EBITDA"]),
                         {"Revenue": 1250.5, "EBITDA": 300.0})


if __name__ == "__main__":
    unittest.main()
