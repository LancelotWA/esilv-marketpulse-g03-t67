# TD04 - Clement

## Part 2 - Starting point

```bash
git status
python src/main.py
git branch
```

Result: [screen/1.png](screen/1.png)

I'm on main, up to date with origin/main and nothing to commit. The program runs but there are no dates yet, only the closes.

## Part 3 - Create the branch

```bash
git switch -c clement_TD4
git branch
```

Result: [screen/2.png](screen/2.png)

The \* is on clement_TD4 so I'm working on the new branch and main doesn't change.

## Part 4 - The feature

I added get_first_date and get_last_date in src/main.py and 2 prints in display_market_summary.

```python
def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]
```

```bash
git status
git diff
```

Result: [screen/3_gitdiff1.png](screen/3_gitdiff1.png) and [screen/3_gitdiff2.png](screen/3_gitdiff2.png)

src/main.py is modified but not staged. In the diff we see the 2 prints and the 2 new functions.

## Part 5 - Commit on the branch

```bash
git add src/main.py
git diff --staged
```

Result: [screen/4.png](screen/4.png)

After git add, git diff shows nothing and git diff --staged shows the change that will be committed.

```bash
git commit -m "feat: display first and last observation dates"
git status
git log --oneline -5
```

Result: [screen/5.png](screen/5.png)

Commit 939f1e4 is on clement_TD4. main is still on edc6b22 (add TD04) so the feature is not in main yet.

## Part 6 - Compare with main

```bash
git log --oneline --graph --decorate --all
git diff main..clement_TD4
```

Results: [screen/6.png](screen/6.png) and [screen/7.png](screen/7.png)

In the graph clement_TD4 is 1 commit ahead of main.

- What is on the branch: the 2 date functions and the 2 prints.
- Why it's not in main: the commit was made on clement_TD4 and nothing was merged yet.
- If we abandon the branch: main stays the same and the feature is lost.

## Part 7 - Merge into main

```bash
git switch main
git branch
git merge clement_TD4
git log --oneline --graph --decorate --all
```

Results: [screen/8.png](screen/8.png) and [screen/9.png](screen/9.png)

Git says "Fast-forward". main didn't move since I created the branch, so git just moved main to 939f1e4, no merge commit. In the graph main and clement_TD4 are on the same commit and the history is still linear.

When I ran the program it crashed because I used :.2f on the dates. :.2f is for numbers and a date is a string, so I removed it.

```bash
python src/main.py
```

Result: [screen/10.png](screen/10.png)

Now the dates are displayed for AAPL and SP500 (2026-09-01 to 2026-09-30).

## Part 8 - Delete the branch

Before deleting: [screen/11.png](screen/11.png) (merge + graph, main and clement_TD4 on 939f1e4).

```bash
git branch -d clement_TD4
git branch
git log --oneline --graph --decorate --all
```

Result: [screen/12.png](screen/12.png)

The branch is deleted with -d (no need to force because it was merged). The commit 939f1e4 is still in main, only the name of the branch is gone.

Then I committed the fix on a branch fix/observation-dates-format and merged it the same way.

Result: [screen/13.png](screen/13.png)

main is 2 commits ahead of origin/main (939f1e4 feat and 48ad1d8 fix).

## Part 9 - Merge conflicts

A conflict is when 2 branches change the same lines and git can't choose which one to keep. Git puts both versions in the file between <<<<<<< ======= >>>>>>> and we have to choose, remove the markers, git add and commit.

In our team Lancelot did the same feature and merged it in origin/main (PR #3). When I did git pull origin main there was no conflict, but the functions and the prints were there twice. Git didn't see a conflict because we didn't write our code on the same lines, so it kept both. That's why you have to run the program after a merge and not just trust git.

His version was already on origin/main so I put my main back on it with git reset --hard origin/main.

## Part 10 - Validation

```bash
python src/main.py
```

Result: [screen/14.png](screen/14.png)

The program still works and the dates are displayed.

This report is on the branch clement_evidence_TD4 and goes into main with a PR.
