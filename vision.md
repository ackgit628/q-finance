ACTION PLAN

I want to be build a quantitative model that will periodically evaluate parametric scores for a group of stocks.
Scores will be calculated for key factors such as quality, growth, value, momentum, etc.
Need to reasearch how these scores will be calculated.

Next, we need to score the entire universe of stocks. Will need to create a database at some point.
Then we pick a portfolio of 25 stocks as per our strategy.
Quality + Growth and Value + Momentum can be a great case study.
We may need to perform some backtests as well before investing.

Steps to achieve this vision (in no particular order)
1.  Learn about the various data sources, APIs. Get familiar with API documentation and identify useful resources specific to our use case. Gather better understanding on fundamental data, market sentiment, alternative data.
2.  Create a database and populate fundamental data. Ideally, we want to be able to calculate scores derived from a function of price and fundamental data. Check the feasibility, is this approach more efficient, as compared to fetching data directly from API.
3.  Put the different pieces of the puzzle together. Feed the data from the API into the database, and write the code to calculate the composite scores and output the top 25 picks.
4.  Observe performance for 6 months, rebalance, optimize strategy, set take profit and stop loss values. Evaluate system robustness by comparing quant scores from SeekingAlpha, Morningstar, other analysts.
5.  Perform backtests and identify which startegy works best during different market cycles. Study in greater detail how to identify market cycles, other promising factor strategies such as low volatility.