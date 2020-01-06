import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader import data as wb

STCK = wb.DataReader('VFINX', data_source='yahoo', start='2019-1-1')
STCK['simple_return'] = (STCK['Adj Close'] / STCK['Adj Close'].shift(1)) - 1
print(STCK['simple_return'])

STCK['simple_return'].plot(figsize = (8,5))
#plt.show() # use this to show in a graph. 

# multiplied by 250 becasue there is an average of 250 days on a calendar year. So just a small trick.. 
avg_returns_a = STCK['simple_return'].mean() * 250
print (str(round(avg_returns_a, 2) * 100) + '%')
