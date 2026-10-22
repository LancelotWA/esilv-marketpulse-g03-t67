"""MarketPulse analytics: pure functions for comparison (TD07)."""


def index_by_date(prices):
    """Return a dict mapping each date to its observation"""
    return {row["date"]: row for row in prices}


def align_series(instrument_prices, benchmark_prices):
    """Keep only the dates present in both series, sorted chronologically"""
    instrument_by_date = index_by_date(instrument_prices)
    benchmark_by_date = index_by_date(benchmark_prices)
    common_dates = sorted(instrument_by_date.keys() & benchmark_by_date.keys())

    aligned_instrument = [instrument_by_date[date] for date in common_dates]
    aligned_benchmark = [benchmark_by_date[date] for date in common_dates]
    return aligned_instrument, aligned_benchmark


def calculate_period_return(prices):
    """Return the total return over the period in %"""
    if not prices:
        raise ValueError("cannot compute a return on an empty series")

    first_close = float(prices[0]["close"])
    last_close = float(prices[-1]["close"])

    if first_close == 0:
        raise ValueError("first close is zero, return is undefined")

    return ((last_close / first_close) - 1.0) * 100.0


def calculate_base_100(prices):
    """Return the series normalized so that the first point equals 100"""
    first_close = float(prices[0]["close"])

    if first_close == 0:
        raise ValueError("first close is zero, base 100 is undefined")

    base_100 = []
    for row in prices:
        value = (float(row["close"]) / first_close) * 100.0
        base_100.append({"date": row["date"], "ticker": row["ticker"], "value": value})

    return base_100


def calculate_relative_performance(instrument_return, benchmark_return):
    """Return the instrument's outperformance vs its benchmark in %"""
    return instrument_return - benchmark_return
