The goal of this TD is to build src/providers/bloomberg_provider.py from the TD09 mapping, and to add build_market_snapshot(...) in src/main.py. We had no live access so the mode is APPROVED_SAMPLE, and the output does not claim live Bloomberg connectivity.

In bloomberg_provider.py AAPL is mapped to AAPL US Equity and SP500 to SPX Index. The provider reads bloomberg_reference_sample.json and renames the teaching keys (observation_date, close_value...) to the canonical fields, with the ticker kept as AAPL or SP500. The normalized rows are identical to bloomberg_reference_expected.json.

In main.py, build_market_snapshot(...) reuses align_series() and the analytics from TD07 without any Bloomberg-specific calculation, and main() only prints the snapshot. The file keeps if __name__ == "__main__": main() so TD11 can import it.

On the branch feature/bloomberg-provider, I add the two files, commit and push ([photos/1.png](photos/1.png)). The working tree is clean and up to date with the remote branch ([photos/2.png](photos/2.png)).

python src/main.py shows Provider Bloomberg stage and Access mode APPROVED_SAMPLE, with AAPL +6.48%, SP500 +2.15% and a relative performance of +4.33 points ([photos/3.png](photos/3.png)).

The PR is then reviewed and merged into main.
