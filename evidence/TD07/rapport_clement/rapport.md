# TD07 - Clement

The goal of this TD is to build `src/analytics.py`, a module of pure functions that compares AAPL with its benchmark SP500, and to call it from `src/main.py`. We are 2 in the team: Lancelot created the stubs and wrote `align_series`, `calculate_relative_performance` and the `main.py` integration. I wrote `index_by_date`, `calculate_period_return` and `calculate_base_100`, and I reviewed the PR.

## Step 1 - Get the branch with the stubs

```bash
git fetch origin
git switch feature/analytics
git branch
git pull
```

Result: [screen/1.png](screen/1.png)

The branch `feature/analytics` created by Lancelot is now local, and the * is on it.

Result: [screen/2.png](screen/2.png)

`src/analytics.py` contains the 5 empty functions (`raise NotImplementedError`).

## Step 2 - index_by_date

```bash
git pull
git add src/analytics.py
git commit -m "feat(analytics): implement index_by_date"
git pull
git push
```

Result: [screen/3.png](screen/3.png)

`index_by_date` returns a dict `{date: row}`, so a row can be found directly by its date. I did it first because `align_series` uses it. Commit `e7efca9` is pushed.

## Step 3 - calculate_period_return

Result: [screen/4.png](screen/4.png)

`calculate_period_return` computes `((last_close / first_close) - 1) * 100` and raises an error on an empty series or a first close at 0. Commit `04dc58d`. The `git pull` merged Lancelot's `align_series` automatically, without conflict.

## Step 4 - calculate_base_100

Result: [screen/5.png](screen/5.png)

`calculate_base_100` returns a list of `{date, ticker, value}` with `value = close / first_close * 100`, so the first point is 100.0. Commit `629defe`.

## Step 5 - main.py integration

```bash
git pull
```

Result: [screen/6_pullmain.png](screen/6_pullmain.png)

The pull brings Lancelot's commit on `src/main.py` (+34 lines).

Result: [screen/7.png](screen/7.png)

`display_comparison` aligns the 2 series, computes the returns, the relative performance and the base 100, and does all the printing. `analytics.py` stays pure.

Result: [screen/8_validationresult.png](screen/8_validationresult.png)

The output matches the expected values: 21 sessions, +6.48% / +2.15%, +4.33 percentage points, base 100 at 106.48 / 102.15.

## Step 6 - Review and merge

Result: [screen/9.png](screen/9.png)

Lancelot reviewed my functions, and I reviewed his part (`align_series`, `calculate_relative_performance`, `main.py`) and approved. Then I merged PR #10 into main.

## Step 7 - Sync main

```bash
git switch main
git pull
git log --oneline -5
python src/main.py
```

Result: [screen/10.png](screen/10.png)

My local main was 9 commits behind, the pull is a fast-forward to `6d8a627` (merge of PR #10).

Result: [screen/11.png](screen/11.png)

On main, `python src/main.py` shows the same comparison as on the branch.
