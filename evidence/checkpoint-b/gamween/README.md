# Checkpoint B

## Student

- Name: Sofiane Ben Taleb
- GitHub: @gamween

## Contribution

- Branch: feature/yahoo-provider
- Main commits:
  - 9d0733b chore(deps): add yfinance to requirements
  - 658b095 feat(yahoo): add Yahoo Finance provider returning canonical rows
  - 4915124 feat(main): switch market data between the csv and yahoo providers
  - cb2cc17 feat(main): fall back to the CSV provider when Yahoo is unavailable
- Pull Request: #14
- Reviewed Pull Request: to be completed

## Work completed

I was the Yahoo lead for TD08 (team of 3, Lancelot is the reviewer of my PR).

- Added `yfinance` to `requirements.txt`.
- Wrote `src/providers/yahoo_provider.py`: `fetch_yahoo_prices(canonical_ticker, lookback, interval)` translates the MarketPulse ticker to the Yahoo symbol (`AAPL -> AAPL`, `SP500 -> ^GSPC`), downloads the history and returns canonical rows (same shape as `prices.csv`): `date` as a `YYYY-MM-DD` string, `ticker` as the canonical one, OHLC as `float`, `volume` as `int`, sorted by date.
- Added the provider switch in `src/main.py` (`PROVIDER = "yahoo"` or `"csv"`). Only the loading of the two series changed, the TD07 comparison code is the same and `src/analytics.py` was not touched.
- Optional 2: if Yahoo fails, `main.py` prints a notice and falls back to the CSV provider, and the `Provider` line shows the provider that really gave the data.

## Main difficulty

When the network is down, yfinance does not always fail the same way: sometimes it raises a connection error, sometimes it only logs "possibly delisted" and returns an empty DataFrame. The adapter turns both cases into a `YahooProviderError`, otherwise the CSV fallback would never trigger on an empty answer. I also used `yf.Ticker(...).history()` instead of `yf.download()`, because `download` returns columns like `('Close', 'AAPL')` instead of `Close`.

## Evidence

- 01_pull_request.png - PR #14 `feat: add Yahoo Finance market data provider`, author gamween, `feature/yahoo-provider` into `main`
- 02_code_review.png - to be completed
- 03_yahoo_market_data.png - live retrieval through the Yahoo provider (2026-11-20): symbol mapping, then 23 canonical rows for `AAPL` and for `SP500` (not `^GSPC`)
- 04_instrument_benchmark.png - `python src/main.py` on Yahoo Finance (live): AAPL and S&P 500 over the same lookback (1 month) and interval (daily), 23 aligned sessions, AAPL +2.86%, SP500 -6.96%, relative performance +9.82 points
