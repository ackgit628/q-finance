import yfinance as yf
from yfinance import EquityQuery
import json

q = EquityQuery('and', [
       EquityQuery('gt', ['intradaymarketcap', 10000000000]),
       EquityQuery('eq', ['region', 'in']),
       EquityQuery('eq', ['exchange', 'NSI'])
])
x = 0
a = []
response = yf.screen(q, offset=0, size=250, sortField='intradaymarketcap', sortAsc=False)

while x<response['total']:
    response = yf.screen(q, offset=x, size=250, sortField='intradaymarketcap', sortAsc=False)
    for quote in response['quotes']:
        a.append(quote['symbol'])
    x+=250
# Print the response to understand its structure
print(len(a))
print(a)

# # Assuming the quotes are in the 'quotes' key of the response dictionary
# if 'quotes' in response:
#     for quote in response['quotes']:
#         print(quote['symbol'])

# json_filename = 'screen.json'
# with open(json_filename, 'w') as json_file:
#     json.dump(response, json_file, indent=4, default=str)

# print("Data saved to", json_filename)

# Run the screen query to fetch equities meeting the criteria.
# try:
#     result = yf.screen(q)
#     print("Screened equities with marketCap > 0:")
#     print(result)
# except Exception as e:
#     print("An error occurred during screening:", e)