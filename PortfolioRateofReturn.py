# get all your fuckin imports
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

#get your portfolio tickets
# I am going to get my ticker for stock and mutual funds seperate to compare and see what is performing well

stck_tickers = ['AAPL', 'ENB', 'MDT', 'NKE', 'BRK-B']
myPortfolio = pd.DataFrame()
for t in stck_tickers:
    myPortfolio[t] = wb.DataReader(t, data_source='yahoo', start='2019-1-4')['Adj Close']

# The following steps is when we plot a graph, we need all the charts to start from the same point
myPortfolio.iloc[0] #alternatively you can use the function mydata.loc['2019-1-1'], but using iloc is easier
(myPortfolio/myPortfolio.iloc[0] *100).plot(figsize = (15, 6))

#if you dont do the previous line, see the below line to see how it all starts and we have no way to do 
# the perfomance. It is just a trick. 
#myPortfolio.plot(figsize = (15, 6))


plt.show()

returns = (myPortfolio / myPortfolio.shift(1)) - 1 #this is just daily returns
annual_returns = returns.mean() * 250 * 100 #yearly returns assuming there are 250 trading days per year. 

print(annual_returns)

weights = np.array([0.41, 0.21, 0.11, 0.18, 0.09])
stckPortfolio = str(round(np.dot(annual_returns, weights), 2)) + '%'  #this is a numpy method to multiply 2 array's 
print ('My Stock Porfolio Returs - : ' + stckPortfolio)

############################### NOW MY MUTUAL FUNDS ########### ASK PRIYA TO WRITE IT BETTER #######################

mf_tickers = ['VFIAX', 'VDIGX', 'VIG', 'VWELX', 'VWIGX']
myMFPortfolio = pd.DataFrame()
for t in mf_tickers:
    myMFPortfolio[t] = wb.DataReader(t, data_source='yahoo', start='2019-1-4')['Adj Close']

mfReturns = (myMFPortfolio / myMFPortfolio.shift(1)) - 1 #this is just daily returns
annual_MFreturns = mfReturns.mean() * 250 * 100 #yearly returns assuming there are 250 trading days per year. 

print(annual_MFreturns)

mfWeights = np.array([0.41, 0.16, 0.02, 0.25, 0.17])
mfPortfolio = str(round(np.dot(annual_MFreturns, mfWeights), 2)) + '%'  #this is a numpy method to multiply 2 array's 
print ('My Mutual Porfolio Returs - : ' + mfPortfolio)

################# TOTAL PORTFOLIO ####################### USE FUNCTION CALLS TO MINIMIZE THE CODE REPEAT ####

tot_tickers = ['AAPL', 'ENB', 'MDT', 'NKE', 'BRK-B','VFIAX', 'VDIGX', 'VIG', 'VWELX', 'VWIGX']
myTotPortfolio = pd.DataFrame()
for t in tot_tickers:
    myTotPortfolio[t] = wb.DataReader(t, data_source='yahoo', start='2010-1-4')['Adj Close']

totReturns = (myTotPortfolio / myTotPortfolio.shift(1)) - 1 #this is just daily returns
annual_Totreturns = totReturns.mean() * 250 * 100 #yearly returns assuming there are 250 trading days per year. 

print(annual_Totreturns)

totWeights = np.array([0.12, 0.06, 0.03, 0.05, 0.03, 0.29, 0.11, 0.01, 0.17, 0.12 ])
totPortfolio = str(round(np.dot(annual_Totreturns, totWeights), 2)) + '%'  #this is a numpy method to multiply 2 array's 
print ('My Mutual Porfolio Returs - : ' + totPortfolio)

