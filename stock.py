import yfinance as yf

stock_list = ['AAPL','TSLA','GOOGL','BABA','TCEHY','TSM']

for ticker in stock_list:
	temp = yf.Ticker(ticker)
	print(ticker, ' close price is: ',temp.info["previousClose"])
	print(ticker, ' PE is: ',temp.info["forwardPE"])


#0 0 * * * python3 /opt/scripts/stocks.py | mail -s "Stock Report" -a From:"Di's Daily Report<smtp@di.family>" carl.di27@gmail.com
