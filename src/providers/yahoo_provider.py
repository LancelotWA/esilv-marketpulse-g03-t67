"""MarketPulse Yahoo Finance provider: remote prices as canonical rows (TD08)."""

import yfinance as yf


# MarketPulse canonical ticker -> Yahoo Finance symbol.
CANONICAL_TO_YAHOO = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}

YAHOO_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]


class YahooProviderError(RuntimeError):
    """Raised when Yahoo Finance cannot return usable data (network, empty result)."""


def to_yahoo_symbol(canonical_ticker):
    """Translate a canonical MarketPulse ticker to its Yahoo Finance symbol"""
    if canonical_ticker not in CANONICAL_TO_YAHOO:
        raise ValueError(f"no Yahoo Finance symbol mapped for ticker {canonical_ticker}")
    return CANONICAL_TO_YAHOO[canonical_ticker]


def fetch_yahoo_prices(canonical_ticker, lookback="1mo", interval="1d"):
    """Return the Yahoo Finance history of a ticker as canonical rows, sorted by date"""
    symbol = to_yahoo_symbol(canonical_ticker)

    try:
        history = yf.Ticker(symbol).history(
            period=lookback,
            interval=interval,
            auto_adjust=False,
        )
    except Exception as error:
        raise YahooProviderError(f"Yahoo Finance request failed for {symbol}: {error}") from error

    if not history.empty:
        history = history.dropna(subset=YAHOO_COLUMNS)
    if history.empty:
        raise YahooProviderError(
            f"no Yahoo Finance data for {symbol} (lookback={lookback}, interval={interval})"
        )

    rows = []
    for timestamp, row in history.iterrows():
        rows.append({
            "date": timestamp.strftime("%Y-%m-%d"),
            "ticker": canonical_ticker,
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        })

    return sorted(rows, key=lambda row: row["date"])
