from flask import Flask, render_template,request, flash, redirect, session
from pandas_datareader._utils import RemoteDataError
from pandas_datareader import data as wb
import pandas as pd

def getAdjustedClose(tickers):
    """ gets data for all tickers entered by on adjusted close"""
    #add start parameter to choose date range
    cap_tickers = [cap.upper() for cap in tickers]
   
    try:
        data = pd.DataFrame()
        for t in cap_tickers:
            data[t] = wb.DataReader(t, data_source='yahoo', start='1995-1-1')['Adj Close']

        return (data)
    except RemoteDataError:
        #flash a message if error
        return redirect('/')
