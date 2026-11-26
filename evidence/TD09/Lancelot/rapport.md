The goal of this TD is to write docs/BLOOMBERG_FIELD_MAPPING.md, the mapping that TD10 will use to build the Bloomberg provider. We had no live access so the mode is APPROVED_SAMPLE.

I update main and run main.py ([photos/0.png](photos/0.png)), then I create the branch docs/bloomberg-mapping ([photos/1.png](photos/1.png))

In bloomberg_reference_sample.json AAPL US Equity is mapped to AAPL ([photos/2.png](photos/2.png)) and SPX Index to SP500, with a volume always at 0 because it is an index ([photos/3.png](photos/3.png)). The keys like close_value are teaching keys, not Bloomberg fields.

I write the mapping document ([photos/4.png](photos/4.png)), commit ([photos/5.png](photos/5.png)) and push ([photos/6.png](photos/6.png)). The PR #17 is reviewed and merged into main.
