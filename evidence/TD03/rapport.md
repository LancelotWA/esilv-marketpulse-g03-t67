# TD03

## Starting point

The TD02 code was already committed and merged by Lancelot (PR #1), so there was no TD02 change left in the working tree.
As the lab suggests in "Nothing to commit", I used a small meaningful improvement of `src/main.py` instead: clean up the TD02 helpers without changing the behaviour.

## Part 2 - Git identity

```bash
git config user.name
git config user.email
```

Result: [screen/01_git_identity.png](screen/01_git_identity.png)

The identity is mine (Sofiane, @gamween), so the commit is attributable to me.

## Part 3 & 4 - git status and git diff

```bash
git status
git diff
```

Result: [screen/02_git_status_diff.png](screen/02_git_status_diff.png)

`git status` shows `src/main.py` as modified but not staged. `git diff` shows the unstaged lines: the `-` lines are removed, the `+` lines are added.

## Part 5 - Stage the intended change

```bash
git switch -c refactor/clean-close-helpers
git add src/main.py
git status
git diff --staged
```

Result: [screen/03_git_add_staged.png](screen/03_git_add_staged.png)

Only `src/main.py` was staged (no `git add .`). It now appears under "Changes to be committed", and `git diff --staged` shows exactly what goes into the commit.

- `git diff` = unstaged changes
- `git diff --staged` = changes selected for the next commit

The branch was created so the change can go through a Pull Request on the team repository.

## Part 6 - Commit

MarketPulse still runs before committing:

```bash
python3 src/main.py
```

Result: [screen/04_run_before_commit.png](screen/04_run_before_commit.png) - same output as TD02 (21 observations, 250.00 -> 266.20 USD, 6600.00 -> 6742.00).

```bash
git commit -m "refactor: simplify close helpers and fix PEP 8 formatting"
```

## Part 7 - Read the history

```bash
git status
git log --oneline -5
git show HEAD
```

Results: [screen/05_git_status_log.png](screen/05_git_status_log.png) and [screen/06_git_show.png](screen/06_git_show.png)

After the commit the working tree is clean, and the new commit `71c947f` is at the top of the log, on top of the TD02 merge.

### Explain the commit

1. Which files changed? Only `src/main.py`.
2. What does the diff represent?
   - `get_first_close` and `get_last_close` return `float(prices[...]["close"])` directly, instead of storing the close in a variable named `row` (it was a value, not a row).
   - `display_market_summary(...) :` becomes `display_market_summary(...):`, and the trailing whitespace is removed.
   - Two blank lines between functions, like the rest of the file (PEP 8).
3. Why is the message appropriate? The behaviour does not change (same output), the code is only clearer, so it is a `refactor:` and the message says what was done.
4. Who is the author? Sofiane (@gamween), as shown in `git show HEAD`.
