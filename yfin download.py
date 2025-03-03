import yfinance as yf

tickers = ['TCS.NS', 'RELIANCE.NS', 'HDFCBANK.NS']
data = yf.download(tickers, start='2020-01-01', end='2024-12-31', interval='1d')

print(data.head())

json_filename = 'download.json'
data.to_json(json_filename, orient='split', date_format='iso')

print("Data saved to", json_filename)