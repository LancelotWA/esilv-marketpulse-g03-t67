"""MarketPulse analytics: pure functions for comparison (TD07)."""


def index_by_date(prices):
    """Return a dict mapping each date to its observation"""
    return {row["date"]: row for row in prices}


def align_series(instrument_prices, benchmark_prices):
    raise NotImplementedError  # Owner: Lead


def calculate_period_return(prices):
    raise NotImplementedError  # Owner: see team table


def calculate_base_100(prices):
    raise NotImplementedError  # Owner: see team table


def calculate_relative_performance(instrument_return, benchmark_return):
    """Return the instrument's outperformance vs its benchmark in %"""
    return instrument_return - benchmark_return
