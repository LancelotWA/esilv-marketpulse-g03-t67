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
    raise NotImplementedError  # Owner: see team table


def calculate_base_100(prices):
    raise NotImplementedError  # Owner: see team table


def calculate_relative_performance(instrument_return, benchmark_return):
    """Return the instrument's outperformance vs its benchmark in %"""
    return instrument_return - benchmark_return
