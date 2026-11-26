"""MarketPulse Bloomberg provider: Bloomberg-stage input as canonical rows (TD10).

Mapping source: docs/BLOOMBERG_FIELD_MAPPING.md (TD09).
Access mode: APPROVED_SAMPLE (no live Bloomberg connectivity).
"""

import json
from pathlib import Path


ACCESS_MODE = "APPROVED_SAMPLE"

SAMPLE_FILE = Path(__file__).resolve().parents[2] / "data" / "sample" / "bloomberg_reference_sample.json"

BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}


def load_raw_bloomberg_history(identifier):
    """APPROVED_SAMPLE raw input: return the fixture series of a Bloomberg identifier"""
    with open(SAMPLE_FILE, encoding="utf-8") as file:
        sample = json.load(file)

    for series in sample["series"]:
        if series["provider_identifier"] == identifier:
            return series

    raise ValueError(f"no approved sample series for {identifier}")


def normalize_bloomberg_history(raw_data, canonical_ticker):
    """Rename the teaching wrapper keys to the canonical row fields"""
    rows = []
    for observation in raw_data["observations"]:
        rows.append({
            "date": observation["observation_date"],
            "ticker": canonical_ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        })
    return rows


def fetch_bloomberg_prices(canonical_ticker):
    """Return the Bloomberg-stage history of a canonical ticker as canonical rows"""
    identifier = BLOOMBERG_IDENTIFIERS[canonical_ticker]
    raw_data = load_raw_bloomberg_history(identifier)
    return normalize_bloomberg_history(raw_data, canonical_ticker)
