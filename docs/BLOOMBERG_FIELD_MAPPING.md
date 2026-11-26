# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

- Source: `data/sample/bloomberg_reference_sample.json`
- Reference: `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md` (not available in the repository; the mapping follows the sample `schema_note` and `data/sample/bloomberg_reference_expected.json`)
- Live connectivity: not demonstrated

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | Teaching wrapper key. ISO string `YYYY-MM-DD`. |
| ticker | application mapping | `AAPL` or `SP500`, taken from the series `canonical_ticker`, never from `provider_identifier`. |
| open | `open_value` | Teaching wrapper key. |
| high | `high_value` | Teaching wrapper key. |
| low | `low_value` | Teaching wrapper key. |
| close | `close_value` | Teaching wrapper key. |
| volume | `volume_value` | Teaching wrapper key. Always `0` for SP500 (an index has no traded volume). |

```text
teaching wrapper key
!=
Bloomberg LIVE field mnemonic
```

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: `AAPL US Equity` -> `AAPL`
- Benchmark identifier: `SPX Index` -> `SP500`
- Date representation: ISO string `YYYY-MM-DD` in `observation_date`, daily, trading days only
- Input structure: root object with a `series` list; each series has `role`, `canonical_ticker`, `provider_identifier` and an `observations` list
- Missing fields: none
- Special normalization notes:
  - take `ticker` from `canonical_ticker`, so `analytics.py` only receives `AAPL` and `SP500`;
  - rename the wrapper keys to the canonical fields without changing the values;
  - keep `volume = 0` for SP500.
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`
