import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

weight = []

def percentOfPortfolio(total, amounts):
    """ calculates the percentage each stock in a portfolio makes up"""
    # get names of each stock to display
    for k,v in amounts.items():
        print(f'TICKER = {k}: Total Value: {v} Percentage: {round(v / total * 100, 2) }%' )

        weight.append(round(v / total * 100, 2))
    print(weight)
    return np.array([weight])
        

percentOfPortfolio(5639.19, {'APLE': 158.60, 'DNP': 136.23, 'GAIN': 182.86,
'GLAD': 109.80, 'O': 3034.16, 'SPYD': 1527.48, 'VIG': 307.10, 'CASH': 182.94})