"""MarketPulse analytics: pure functions for comparison (TD07)."""


def index_by_date(prices):
    """Return a dict mapping each date to its observation"""
    return {row["date"]: row for row in prices}


def align_series(instrument_prices, benchmark_prices):
    raise NotImplementedError  # Owner: Lead


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
    raise NotImplementedError  # Owner: see team table


def calculate_relative_performance(instrument_return, benchmark_return):
    """Return the instrument's outperformance vs its benchmark in %"""
    return instrument_return - benchmark_return
