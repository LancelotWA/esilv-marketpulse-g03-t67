from pathlib import Path
import csv
import json
import sys

# Make the project root importable so "python src/main.py" can resolve "src.analytics".
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.analytics import (
    align_series,
    calculate_period_return,
    calculate_base_100,
    calculate_relative_performance,
)
from src.providers.yahoo_provider import YahooProviderError, fetch_yahoo_prices
from src.providers.bloomberg_provider import ACCESS_MODE as BLOOMBERG_ACCESS_MODE, fetch_bloomberg_prices


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
PROVIDER = "bloomberg"  # "bloomberg", "yahoo" or "csv"
LOOKBACK = "1mo"
INTERVAL = "1d"
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"
PROVIDER_LABELS = {
    "csv": "CSV (local sample)",
    "yahoo": "Yahoo Finance (live)",
    "bloomberg": "Bloomberg stage",
}
ACCESS_MODES = {
    "csv": "LOCAL_SAMPLE",
    "yahoo": "LIVE",
    "bloomberg": BLOOMBERG_ACCESS_MODE,
}


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def load_market_series(provider, instrument, benchmark):
    if provider == "yahoo":
        instrument_prices = fetch_yahoo_prices(instrument["ticker"], LOOKBACK, INTERVAL)
        benchmark_prices = fetch_yahoo_prices(benchmark["ticker"], LOOKBACK, INTERVAL)
        return instrument_prices, benchmark_prices

    if provider == "bloomberg":
        instrument_prices = fetch_bloomberg_prices(instrument["ticker"])
        benchmark_prices = fetch_bloomberg_prices(benchmark["ticker"])
        return instrument_prices, benchmark_prices

    if provider == "csv":
        prices = load_prices()
        return filter_prices(prices, instrument["ticker"]), filter_prices(prices, benchmark["ticker"])

    raise ValueError(f"unknown provider {provider}")


def load_market_data(instrument, benchmark):
    """Return the provider actually used and both series, falling back to CSV when Yahoo fails"""
    try:
        return (PROVIDER, *load_market_series(PROVIDER, instrument, benchmark))
    except YahooProviderError as error:
        print(f"Notice: Yahoo Finance unavailable ({error}).")
        print("Notice: falling back to the CSV provider (local sample data).")
        print()
        return ("csv", *load_market_series("csv", instrument, benchmark))


def get_first_close(prices):
    return float(prices[0]["close"])


def get_last_close(prices):
    return float(prices[-1]["close"])

def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]


def get_market(asset):
    return asset["market"]


def get_currency(asset):
    return asset["currency"]



def display_market_summary(asset, prices, show_currency=True):
    currency = f" {asset['currency']}" if show_currency else ""

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Market       : {get_market(asset)}")
    print(f"Currency     : {get_currency(asset)}")
    print(f"Observations : {len(prices)}")
    print(f"First date   : {get_first_date(prices)}")
    print(f"Last date    : {get_last_date(prices)}")
    print(f"First close  : {get_first_close(prices):.2f}{currency}")
    print(f"Last close   : {get_last_close(prices):.2f}{currency}")


def build_market_snapshot(provider=PROVIDER, lookback=LOOKBACK, interval=INTERVAL):
    """Return the shared application result used by the terminal and the dashboard"""
    instruments = load_instruments()
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    provider, instrument_prices, benchmark_prices = load_market_data(instrument, benchmark)
    aligned_instrument, aligned_benchmark = align_series(instrument_prices, benchmark_prices)

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)

    return {
        "provider": provider,
        "access_mode": ACCESS_MODES[provider],
        "lookback": lookback,
        "interval": interval,
        "instrument": instrument,
        "benchmark": benchmark,
        "instrument_prices": instrument_prices,
        "benchmark_prices": benchmark_prices,
        "aligned_sessions": len(aligned_instrument),
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": calculate_relative_performance(instrument_return, benchmark_return),
        "instrument_base_100": calculate_base_100(aligned_instrument),
        "benchmark_base_100": calculate_base_100(aligned_benchmark),
    }


def main():
    snapshot = build_market_snapshot()
    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]

    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print(f"Period      : {LOOKBACK_LABEL}")
    print(f"Interval    : {INTERVAL_LABEL}")
    print(f"Provider    : {PROVIDER_LABELS[snapshot['provider']]}")
    print(f"Access mode : {snapshot['access_mode']}")
    print()
    print("Instrument")
    display_market_summary(instrument, snapshot["instrument_prices"])
    print()
    print("Benchmark")
    display_market_summary(benchmark, snapshot["benchmark_prices"], show_currency=False)
    print()
    print("Comparison")
    print(f"Aligned sessions     : {snapshot['aligned_sessions']}")
    print(f"Instrument return    : {snapshot['instrument_return']:+.2f}%")
    print(f"Benchmark return     : {snapshot['benchmark_return']:+.2f}%")
    print(f"Relative performance : {snapshot['relative_performance']:+.2f} percentage points")
    print()
    print("Base 100")
    print(f"{instrument['ticker']} : 100.00 -> {snapshot['instrument_base_100'][-1]['value']:.2f}")
    print(f"{benchmark['ticker']} : 100.00 -> {snapshot['benchmark_base_100'][-1]['value']:.2f}")


if __name__ == "__main__":
    main()
