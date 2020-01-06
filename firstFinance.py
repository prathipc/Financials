import yfinance as yf
msft = yf.Ticker("MSFT")

#get stockinfo

#print (msft.info)
# get dividends
    #print (msft.actions)

msft.dividends
x = msft.history(period='1mo', 
            interval='1d')

print(x['Open'])

#Other Option to print the close.. from a dataframe!
print (msft.history(period='1mo', 
            interval='1d')['Close'])

#STCK['simple_return'].mean()

#show financials
msft.financials
#print(msft.quarterly_financials)