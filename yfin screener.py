import yfinance as yf
from yfinance import EquityQuery
import json

q = EquityQuery('and', [
       EquityQuery('gt', ['intradaymarketcap', 0]),
       EquityQuery('eq', ['region', 'in']),
       EquityQuery('eq', ['exchange', 'NSI'])
])
response = yf.screen(q, offset=250, size=250, sortField='intradaymarketcap', sortAsc=True)

for quote in response.quotes:
    print(quote['symbol'])

# json_filename = 'screen.json'
# with open(json_filename, 'w') as json_file:
#     json.dump(response, json_file, indent=4)

# print("Data saved to", json_filename)

# Run the screen query to fetch equities meeting the criteria.
# try:
#     result = yf.screen(q)
#     print("Screened equities with marketCap > 0:")
#     print(result)
# except Exception as e:
#     print("An error occurred during screening:", e)