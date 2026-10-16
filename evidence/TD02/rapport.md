# TD02

## Part 1

### Answers

1. Which function reads JSON?

load_instruments() opens data/sample/instruments.json with json.load(). It gives a dict with 2 keys: instrument and benchmark.

2. Which function reads CSV?

load_prices() opens data/sample/prices.csv with csv.DictReader. It gives a list of dicts, one per row.

3. Which one selects one ticker?

filter_prices(prices, ticker) keeps only the rows with the ticker we want (AAPL or SP500) with a list comprehension.

4. Which one coordinates execution?

main() loads the data, filters the 2 series and prints the results.

5. Where are the input files stored?

In data/sample/ (DATA_DIR in the code). It's a relative path so we have to run the program from the root of the repo.


## Part 2&3 - JSON CSV & conversion

### JSON -> dictionary

We added temporary prints in main() to see the type and the keys of instruments.

Result: [screen/part2_json.png](screen/part2_json.png)

instruments is a dict with 2 keys: instrument and benchmark. Each value is also a dict.

### CSV -> list of dictionaries

Result: [screen/part2_csv.png](screen/part2_csv.png)

We see list then dict so prices is a list of dicts. prices[0] is the first row of the CSV.


## Part 4

Understanding list comprehensions (shorter than a loop). AAPL and SP500 have 21 rows each (see part5.png).

## Part 5

Two functions:

```python
def get_first_close(prices):
    row = prices[0]["close"]
    return float(row)

def get_last_close(prices):
    row = prices[-1]["close"]
    return float(row)
```

In the main function:

```python
print("AAPL : ", get_first_close(instrument_prices), get_last_close(instrument_prices))
print("SP500 : ", get_first_close(benchmark_prices), get_last_close(benchmark_prices))
```

In the terminal: [screen/part5.png](screen/part5.png)

## Part 6 & 8

Here is the function:

```python
def display_market_summary(asset, prices, show_currency=True):
    currency = f" {asset['currency']}" if show_currency else ""

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Observations : {len(prices)}")
    print(f"First close  : {get_first_close(prices):.2f}{currency}")
    print(f"Last close   : {get_last_close(prices):.2f}{currency}")
```

We get the expected result: [screen/part6-8.png](screen/part6-8.png)
