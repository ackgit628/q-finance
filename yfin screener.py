import yfinance as yf
from yfinance import EquityQuery
import time
import logging

# ------------------------------------------------------------
# Set Up Logging
# ------------------------------------------------------------
# Logging is configured to output timestamps and log levels. This helps track the code's progress and diagnose issues.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ------------------------------------------------------------
# Define the Query
# ------------------------------------------------------------
# Here, we build a query using EquityQuery that filters for:
# - intradaymarketcap greater than 10,000,000,000 (i.e., 1000 Cr)
# - region 'in' (India)
# - exchange 'NSI'
q = EquityQuery('and', [
    EquityQuery('gt', ['intradaymarketcap', 10000000000]),
    EquityQuery('eq', ['region', 'in']),
    EquityQuery('eq', ['exchange', 'NSI'])
])

# ------------------------------------------------------------
# Initialize Variables for Pagination
# ------------------------------------------------------------
symbols = []           # List to store fetched ticker symbols
offset = 0             # Starting offset for pagination
page_size = 250        # Number of records per page

# ------------------------------------------------------------
# Initial Request to Determine Total Results
# ------------------------------------------------------------
try:
    response = yf.screen(q, offset=offset, size=page_size, sortField='intradaymarketcap', sortAsc=False)
    total_results = response.get('total', 0)
    logging.info(f"Total results found: {total_results}")
except Exception as e:
    logging.error(f"Failed to fetch initial results: {e}")
    total_results = 0

# ------------------------------------------------------------
# Fetch Data in a Paginated Manner with Error Handling and Rate Limiting
# ------------------------------------------------------------
while offset < total_results:
    try:
        logging.info(f"Fetching results with offset: {offset}")
        response = yf.screen(q, offset=offset, size=page_size, sortField='intradaymarketcap', sortAsc=False)
        quotes = response.get('quotes', [])
        for quote in quotes:
            # Append the symbol if it exists; using .get ensures we avoid KeyError if missing
            symbol = quote.get('symbol')
            if symbol:
                symbols.append(symbol)
        offset += page_size

        # ------------------------------------------------------------
        # Rate Limiting
        # ------------------------------------------------------------
        # Adding a delay prevents overwhelming the API and helps manage request rate limits.
        time.sleep(1)
    except Exception as e:
        logging.error(f"Error while fetching results at offset {offset}: {e}")
        # Depending on your requirements, you might choose to skip this page or break out of the loop.
        break

# Optional: Remove duplicates if they occur
# symbols = list(set(symbols))
# commenting as sorted order is lost

# ------------------------------------------------------------
# Final Output
# ------------------------------------------------------------
# Print the number of unique symbols fetched and the list itself.
print(f"Total unique symbols fetched: {len(symbols)}")
print(symbols)
