# TD05 - Clement

The goal of this TD is to add one feature per student, each on its own branch with its own Pull Request. The PRs stay open and are reviewed and validated by the team in TD06.

My feature is to display market metadata: the market and the currency of each series. They come from the `market` and `currency` fields in `data/sample/instruments.json` (NASDAQ / USD for AAPL, US / USD for SP500).

I added 2 helpers in `src/main.py`:

```python
def get_market(asset):
    return asset["market"]


def get_currency(asset):
    return asset["currency"]
```

and 2 prints in `display_market_summary`, right after the ticker/name line:

```python
    print(f"Market       : {get_market(asset)}")
    print(f"Currency     : {get_currency(asset)}")
```

I only touched `display_market_summary` and not the "Market configuration" block, because that's where my teammate adds the provider. This way our 2 PRs don't change the same lines and can be merged without conflict.

## Step 1 - Start from the latest main

```bash
git switch main
git pull origin main
git rev-parse HEAD
git rev-parse origin/main
```

Result: [screen/1.png](screen/1.png)

Both commands give the same hash `3c4145a` (Add TD05.md), so my local main is on the last commit of the team main. My teammate has the same commit, so we start from the same base.

## Step 2 - Create the branch

```bash
git switch -c feature/display-market-metadata
git branch
```

Result: [screen/2.png](screen/2.png)

The * is on feature/display-market-metadata, so I'm working on my feature branch and not on main.

## Step 3 - Run the program

```bash
python src/main.py
```

Result: [screen/3.png](screen/3.png)

The Market and Currency lines are displayed: NASDAQ / USD for AAPL and US / USD for SP500. The currency is also shown for the benchmark, even if its prices are displayed without it (`show_currency=False`). The rest of the output didn't change.

## Step 4 - Commit and push

(no screen here, otherwise this report could not be in the commit)

```bash
git add src/main.py
git diff --staged
git commit -m "feat: display market metadata"
git push -u origin feature/display-market-metadata
```

The commit message says what the change does. The push creates the branch on GitHub too, not only in local.

## Step 5 - Pull Request

I opened the PR "feat: display market metadata" on GitHub, from my branch to main. I didn't merge it: my teammates have to check and validate it in TD06.
