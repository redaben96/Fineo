# Fineo

**Open financial analytics, built for clarity.**

Fineo is an educational, modular Python toolkit for reproducible financial research. It combines valuation, basic market indicators, economic time-series transformations, company screening, and financial-statement analysis in one lightweight codebase.

> **Privacy and provenance:** This repository contains independently written demonstration code and fabricated sample data. It includes no employer assets, private research, licensed datasets, API keys, or unpublished financial information. No relationship with any financial institution is implied.

## Features

| Module | Capabilities |
| --- | --- |
| Valuation | DCF, P/E implied value, EV/EBITDA implied equity value |
| Financial analysis | Margins, leverage, interest coverage and liquidity ratios |
| Macro analytics | YoY changes, monthly changes, indexed series |
| Market intelligence | Moving averages, RSI and normalized price performance |
| Equity screening | Transparent weighted scoring and rankings |
| Document analysis | Parse simple **text** financial statements using configured patterns |

All examples use synthetic data. The document parser is a rule-based prototype, not an AI model or OCR engine.

## Quick start

Requires Python 3.10+. No third-party packages or accounts needed.

```bash
git clone https://github.com/redaben96/Fineo.git
cd Fineo
python -m unittest discover -s tests -v
python examples/demo.py
```

## Example

```python
from fineo.valuation import dcf_equity_value, pe_implied_equity_value

value = dcf_equity_value(
    free_cash_flows=[12, 14, 16, 18, 20],
    discount_rate=0.10,
    terminal_growth=0.025,
    net_debt=35,
)
print(round(value, 2))
print(pe_implied_equity_value(net_income=10, pe_multiple=15))
```

Values are illustrative and denominated in arbitrary monetary units.

## Structure

- `fineo/` — importable, dependency-free Python modules.
- `examples/demo.py` — executable synthetic demonstration.
- `tests/` — automated correctness tests.
- `docs/ROADMAP.md` — proposed future extensions and limitations.

## Important limitations

This is an **initial public prototype**, not a deployed production application or a validated investment system. No live-market feeds, proprietary valuation datasets, autonomous AI agents, forecasting models, or investment recommendations are included. Ratios and DCF outputs depend on user-supplied accounting definitions and assumptions.

For financial research and education only. **Not investment advice.** Verify all calculations, definitions, and data before real-world use.

## Security and contribution

Do not commit credentials, personal information, internal files, confidential financial statements, or third-party copyrighted datasets. Contributions and issues are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT. See [LICENSE](LICENSE).
