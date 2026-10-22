The goal of this TD is to review the pull request of my teammate before merging it into main. I reviewed the PR #7 of Clément (feature/display-market-metadata).

First I switch to his branch and run main : Market and Currency are displayed for AAPL and SP500 ([photos/img0.png](photos/img0.png)). My Provider line is not there because his branch starts from the old main, before my PR.

On GitHub I check the commits of the PR : there are 2, one for the code and one for the report ([photos/img1.png](photos/img1.png))

Then in Files changed I check the diff : only 2 helpers and 2 prints in src/main.py, plus his report and screens, nothing unrelated ([photos/img2.png](photos/img2.png), [photos/img3.png](photos/img3.png))

I write a comment explaining what I verified ([photos/img4.png](photos/img4.png)), then I submit it as a real review with Approve ([photos/img5.png](photos/img5.png)). No real issue so no correction needed.

Finally I merge the PR, we can see the last activity on main is my merge of PR #7 ([photos/img6.png](photos/img6.png))
