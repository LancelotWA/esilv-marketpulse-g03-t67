# TD04 - Branches + Merge

## Prerequisites

To-do:
- [x] clean main, visible history, MarketPulse runs

```bash
git status
git log --oneline -5
python src/main.py
```

- status shows we're on main up to date with origin/main and nothing to commit
- git log shows the last 5 commits
- python src/main.py runs fine (no dates yet)

Result: [pictures/picture1_git_td04.png](pictures/picture1_git_td04.png)

> TODO: text about the starting point

# Part 1 - Understand branch isolation

A feature branch lets me commit my change without touching `main` which only gets the change once the branch is merged

# Part 2 - Inspect the current branch

To-do:
- [x] check that we are on `main` and the working tree is clean

```bash
git branch
git status
```

- git branch shows the branches (the * is the one we're on)
- status shows we're on main and it's clean

Result: [pictures/picture1_git_td04.png](pictures/picture1_git_td04.png)

We can see the branch is up to date with main

# Part 3 - Create a feature branch

To-do:
- [x] create the feature branch and switch to it
- [x] check with `git branch`

```bash
git switch -c lancelot_WATELLE_TD04
git status
git branch
```

- switch -c creates the branch and moves us on it
- status shows we're on the new branch and it's clean
- git branch shows the new branch (with the *) and main

Results: [pictures/picture2_git_td04.png](pictures/picture2_git_td04.png) and [pictures/picture3_git_td04.png](pictures/picture3_git_td04.png)

We changed the branch name because each student has their own branch, so we name it student_name_TD04 (because it's their own work on the TD)
Note we had to recreate branches (one each) so we could add our report and the screens of the related commands so it's complete

# Part 4 - Implement the small feature

To-do:
- [x] add `get_first_date` / `get_last_date` in `src/main.py`
- [x] display the dates in `display_market_summary`
- [x] check for both Instrument AND Benchmark

```bash
python src/main.py
```

- python src/main.py runs and shows the first and last date for AAPL and SP500

Result: [pictures/picture4_git_td04.png](pictures/picture4_git_td04.png)

We can see the requested display (new lines in the summary)

# Part 5 - Inspect and commit the branch change

To-do:
- [x] inspect the changes
- [x] stage only `src/main.py`
- [x] commit on the branch

```bash
git status
git diff
git add src/main.py
git diff --staged
git commit -m "feat: display first and last observation dates"
git status
git log --oneline -5
```

- status shows a file was modified and not committed (main.py)
- git diff shows the line differences
- add puts the file in the git staging (the next commit will take the changes)
- git diff --staged shows what goes in the commit
- we commit with the right label
- we can see the branch is committed but not pushed (the commit stays on the branch)

Results: [pictures/picture5_git_td04.png](pictures/picture5_git_td04.png) and [pictures/picture6_git_td04.png](pictures/picture6_git_td04.png)

# Part 6 - Compare feature branch and main

To-do:
- [x] display the graph
- [x] compare the branch with main

```bash
git log --oneline --graph --decorate --all
git diff main..lancelot_WATELLE_TD04
```

- git log shows the graph, the branch is 1 commit ahead of main
- git diff shows what's on the branch but not on main (the 8 added lines)

Result: [pictures/picture7_git_td04.png](pictures/picture7_git_td04.png)

Questions:

1. Which change exists on the feature branch?
> Answer: the 2 new functions get_first_date / get_last_date and the 2 prints for the dates

2. Why is that change not yet part of `main`?
> Answer: because the branch isn't merged yet so main doesn't have it

3. What would happen if the branch were abandoned before merge?
> Answer: the change would just stay on the branch and main would never get it

# Part 7 - Merge the feature into main

To-do:
- [x] switch back to main
- [x] merge the branch
- [x] check the graph and that MarketPulse runs

```bash
git switch main
git branch
git merge lancelot_WATELLE_TD04
git log --oneline --graph --decorate --all
python src/main.py
```

- we switch back to main
- git branch shows we're on main
- merge brings the branch into main (fast-forward)
- git log shows main and the branch on the same commit
- python src/main.py runs and shows the dates from main

Results: [pictures/picture8_git_td04.png](pictures/picture8_git_td04.png) and [pictures/picture9_git_td04.png](pictures/picture9_git_td04.png)

Questions:

1. Is the feature now visible from `main`?
> Answer: yes the dates show up when we run it from main

2. Is the feature commit still visible?
> Answer: yes commit 9845c34 is still in the history

3. Did Git perform a fast-forward or create a merge commit?
> Answer: a fast-forward (main just moved forward to the branch commit)

4. What does the graph show?
> Answer: main and the branch point to the same commit 9845c34 so the history stays linear

# Part 8 - Capture Checkpoint A branch evidence, then clean the branch

To-do:
- [x] capture before deletion (branch / merged / graph)
- [x] push + PR #3 on GitHub + merge
- [x] delete the branch (local + remote)

```bash
git branch
git branch --merged
git log --oneline --graph --decorate --all
```

- git branch shows both branches
- git branch --merged shows the branch is merged into main
- git log shows main has the feature commit

Result: [pictures/picture10_git_td04.png](pictures/picture10_git_td04.png)

```bash
git push -u origin lancelot_WATELLE_TD04
git switch main
git pull
git branch -d lancelot_WATELLE_TD04
git push origin --delete lancelot_WATELLE_TD04
git branch
git log --oneline --graph --decorate --all
```

- push sends the branch to github (gives the link for the PR)
- then we merge the PR #3 on github
- pull gets the merge commit from github
- branch -d deletes the local branch
- push --delete deletes it on github
- git branch shows only main is left
- git log shows the commit is still there

Results: [pictures/picture12_git_td04.png](pictures/picture12_git_td04.png) and [pictures/picture11_git_td04.png](pictures/picture11_git_td04.png) (github repo after PR #3)

> TODO: text (the history remains even without the branch name)

# Part 9 - Understand merge conflicts

To-do:
- [ ] explain what a conflict is
- [ ] explain the markers `<<<<<<<` / `=======` / `>>>>>>>`
- [ ] explain the resolution (inspect, choose, remove markers, `git add`, complete merge)

Students should focus on understanding:

- why the conflict occurred
> Answer:

- what `git status` reports
> Answer:

- what the markers mean
> Answer:

- why a human must choose the final content
> Answer:

# Part 10 - CORE validation

To-do:
- [ ] run the 3 commands again at the end and capture them

```bash
git status
git log --oneline --graph --decorate --all
python src/main.py
```

You should be able to explain:

- main
> Answer:
- feature branch
> Answer:
- branch creation
> Answer:
- branch switch
> Answer:
- branch commit
> Answer:
- branch comparison
> Answer:
- merge
> Answer:
- fast-forward
> Answer:
- merge conflict
> Answer:

# Part 11 - Checkpoint A

To-do:
- [ ] `evidence/checkpoint-a/LancelotWA/README.md`
- [ ] `01_terminal_python.png` (from picture9)
- [ ] `02_git_status_log.png` (from picture6)
- [ ] `03_branch_merge.png` (from picture10)

Capture checklist:

- [ ] MarketPulse runs
- [ ] git status is understandable
- [ ] git log shows my work
- [ ] 03_branch_merge.png was captured before the merged feature branch was deleted
- [ ] branch and merge history are understandable, including a valid fast-forward if one occurred
- [ ] evidence is attributable to my GitHub identity
- [ ] no secret appears in a screenshot
