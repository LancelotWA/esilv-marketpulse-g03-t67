The goal of this TD is to build the analytics module of MarketPulse (src/analytics.py) to compare AAPL with its benchmark SP500, then display the comparison in main. We were 2 so I was the lead : I created the stubs, coded align_series and calculate_relative_performance, wired main.py and opened the PR. Clément coded index_by_date, calculate_period_return and calculate_base_100.

First I create the branch feature/analytics from main and the file src/analytics.py with the 5 empty functions, then I commit and push it so Clément can work on the same branch (no screen for this step).

While Clément does his function I code calculate_relative_performance (just instrument_return - benchmark_return), then I pull, commit and push ([screen/picture1.png](screen/picture1.png)). We can see my commit on GitHub ([screen/picture0.png](screen/picture0.png))

Then I pull what Clément did ([screen/picture2.png](screen/picture2.png)) and I check that I can see his index_by_date function in the file ([screen/picture3.png](screen/picture3.png)). I need it because align_series uses it.

I code align_series : it keeps only the dates present in both series, sorted by date. Then I commit, pull and push ([screen/picture4.png](screen/picture4.png))

I pull his two other functions ([screen/picture5.png](screen/picture5.png)) and I check that the file is complete with the 5 functions ([screen/picture6.png](screen/picture6.png))

Then I add the comparison in main.py : a new function display_comparison that aligns the series, computes the returns, the relative performance and the base 100, and I call it in main().

Careful : we had to add `sys.path.insert(0, str(Path(__file__).resolve().parent.parent))` in main.py, otherwise `python src/main.py` gives the error "No module named 'src'". When we run the script Python looks for modules in the src folder and not in the project folder, so it can't find src.analytics.

We can see the new comparison block when we run main, the numbers match the expected values : 21 sessions, AAPL +6.48%, SP500 +2.15%, relative performance +4.33 points ([screen/picture_rendu_new_main.png](screen/picture_rendu_new_main.png))

Then I commit and push main.py ([screen/picture7.png](screen/picture7.png))

I open the PR #10 on GitHub, we can see the 8 commits from both of us. I leave a comment explaining what I checked in Clément's functions ([screen/picture8.png](screen/picture8.png))

Finally the PR is merged into main, we can see the merge of PR #10 as the last commit on main ([screen/picture9.png](screen/picture9.png))
