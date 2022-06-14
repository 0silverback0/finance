import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import stockPortfolioPercentage as gw

def comparePortfolio(tickers):
    """ compare simple returns of stocks good for comparing multiple stocks """
    data = pd.DataFrame()
    for t in tickers:
        data[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']
    
    ## plot and show data
    (data / data.iloc[0] * 100).plot(figsize = (15,6))
    plt.show()

    #normalize data and declare weights
    returns = (data / data.shift(1)) - 1

    ###############
    # this compares the portfolio above compares historical close data
    ###############


    ###this should not be hard coded data get this from stockportfoliopercentage.py
    weights = np.array( [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25])
    #np.dot(returns, weights)

    annual_returns = returns.mean() * 250
    #print(annual_returns)

    portfolio1 = str(round(np.dot(annual_returns, weights), 5) * 100) + '%'
    print(portfolio1)


comparePortfolio(['APLE', 'DNP', 'GAIN', 'GLAD', 'O', 'SPYD', 'VIG'])