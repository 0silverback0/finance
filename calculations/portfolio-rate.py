import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

#calculate a portfolios rate of return

tickers = ['PG', 'MSFT', 'F', 'GE']

myData = pd.DataFrame()

for t in tickers:
    myData[t] = wb. DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

#print(myData.tail())

#print(myData.iloc[0])

#(myData / myData.iloc[0] * 100).plot(figsize = (15,6))
#plt.show()

returns = (myData / myData.shift(1)) - 1
print(returns.head())

weights = np.array([0.25, 0.25, 0.25, 0.25])

np.dot(returns, weights)

annual_returns = returns.mean() * 250
#print(annual_returns)

portfolio1 = str(round(np.dot(annual_returns, weights), 5) * 100) + '%'
print(portfolio1)

weight_2 = np.array([0.4, 0.4, 0.15, 0.05])

portfolio2 = str(round(np.dot(annual_returns, weight_2), 5) * 100) + '%'
print(portfolio2)