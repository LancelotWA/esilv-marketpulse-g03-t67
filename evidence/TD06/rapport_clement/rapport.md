# TD06 - Clement

The goal of this TD is to review another student's Pull Request before merging it. I reviewed Lancelot's PR #6 (`feature/show-provider_label`).

## Step 1 - Read the Pull Request

Result: [screen/1.png](screen/1.png)

PR #6 merges 1 commit (`a262391`) from `feature/show-provider_label` into `main`, with 4 files changed and no conflict.

## Step 2 - Files changed

Result: [screen/2.png](screen/2.png)

The PR changes `src/main.py` (adds `PROVIDER_LABEL = "CSV (local sample)"` and prints it in the Market configuration block) and adds his TD05 report.

## Step 3 - Test his branch

```bash
git fetch origin
git switch -c review-lancelot origin/feature/show-provider_label
git branch
python src/main.py
```

Result: [screen/3.png](screen/3.png)

`Provider : CSV (local sample)` is displayed and the rest of the output is unchanged.

## Step 4 - Review

Result: [screen/4.png](screen/4.png)

I approved the PR with a comment saying what I checked. No real issue was found, so no correction was needed.

## Step 5 - Merge and sync main

After review, both PRs were merged into main. Then I updated my local main:

```bash
git switch main
git pull
```

Result: [screen/5.png](screen/5.png)

My local main is now up to date with the team main (`7688eda`).
