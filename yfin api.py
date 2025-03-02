import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol for Reliance Industries
ticker_symbol = 'RELIANCE.NS'

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch historical market data for the past year
historical_data = ticker.history(period='1y')

# Display the first few rows of the data
print(historical_data.head())

# Plot the closing price history
plt.figure(figsize=(10, 6))
plt.plot(historical_data.index, historical_data['Close'], label='Close Price')
plt.title('Reliance Industries Closing Price History')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()
