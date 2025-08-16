import time
import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol for Reliance Industries
ticker_symbol = 'RELIANCE.NS'

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# # Fetch historical market data for the past year
# historical_data = ticker.history(period='1y')

# # Display the first few rows of the data
# print(historical_data.head())

# # Plot the closing price history
# plt.figure(figsize=(10, 6))
# plt.plot(historical_data.index, historical_data['Close'], label='Close Price')
# plt.title('Reliance Industries Closing Price History')
# plt.xlabel('Date')
# plt.ylabel('Price (INR)')
# plt.legend()
# plt.grid(True)
# plt.show()


# Fetch and print basic information
print("Ticker Info:")
print(ticker.info)
time.sleep(2)  # Wait 2 seconds

# Fetch and print historical market data for the past year
print("\nHistorical Data:")
historical_data = ticker.history(period='1y')
print(historical_data)
time.sleep(2)  # Wait 2 seconds

# Fetch and print actions (dividends, splits)
print("\nActions:")
print(ticker.actions)
time.sleep(2)  # Wait 2 seconds

# Fetch and print dividends
print("\nDividends:")
print(ticker.dividends)
time.sleep(2)  # Wait 2 seconds

# Fetch and print splits
print("\nSplits:")
print(ticker.splits)
time.sleep(2)  # Wait 2 seconds

# Fetch and print financials
print("\nFinancials:")
print(ticker.financials)
time.sleep(2)  # Wait 2 seconds

# Fetch and print quarterly financials
print("\nQuarterly Financials:")
print(ticker.quarterly_financials)
time.sleep(2)  # Wait 2 seconds

# Fetch and print major holders
print("\nMajor Holders:")
print(ticker.major_holders)
time.sleep(2)  # Wait 2 seconds

# Fetch and print institutional holders
print("\nInstitutional Holders:")
print(ticker.institutional_holders)
time.sleep(2)  # Wait 2 seconds

# Fetch and print balance sheet
print("\nBalance Sheet:")
print(ticker.balance_sheet)
time.sleep(2)  # Wait 2 seconds

# Fetch and print quarterly balance sheet
print("\nQuarterly Balance Sheet:")
print(ticker.quarterly_balance_sheet)
time.sleep(2)  # Wait 2 seconds

# Fetch and print cashflow
print("\nCashflow:")
print(ticker.cashflow)
time.sleep(2)  # Wait 2 seconds

# Fetch and print quarterly cashflow
print("\nQuarterly Cashflow:")
print(ticker.quarterly_cashflow)
time.sleep(2)  # Wait 2 seconds

# Fetch and print earnings
print("\nEarnings:")
print(ticker.earnings)
time.sleep(2)  # Wait 2 seconds

# Fetch and print quarterly earnings
print("\nQuarterly Earnings:")
print(ticker.quarterly_earnings)
time.sleep(2)  # Wait 2 seconds

# Fetch and print sustainability
print("\nSustainability:")
print(ticker.sustainability)
time.sleep(2)  # Wait 2 seconds

# Fetch and print recommendations
print("\nRecommendations:")
print(ticker.recommendations)
time.sleep(2)  # Wait 2 seconds

# Fetch and print calendar events
print("\nCalendar:")
print(ticker.calendar)
time.sleep(2)  # Wait 2 seconds

# Fetch and print ISIN (International Securities Identification Number)
print("\nISIN:")
print(ticker.isin)
time.sleep(2)  # Wait 2 seconds

# Fetch and print options expirations
print("\nOptions Expirations:")
print(ticker.options)
time.sleep(2)  # Wait 2 seconds
