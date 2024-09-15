import tpqoa

api = tpqoa.tpqoa("oanda.cfg")

# Get Historical data
dataframe = api.get_history(instrument = "EUR_USD", start = "2024-09-01", end = "2024-09-11",
                granularity = "M5", price = "A")

print (dataframe)

#api.create_order(instrument = "EUR_USD", units = 1000, sl_distance= 0.1)

data = api.get_account_summary()
print (data["balance"])

# Get Historical Data
# Run SMA50, SMA20 Strategy
# Place trade if appropriate
    # Send alert for trade placed
    # Get Data in quick succession (Every 5 seconds)
    # Apply Strategy
        # SMA20/SMA 50
        # abs(SMA20 - SMA50) > 1/2 ATR
        # If difference of last 10 candles also very low, then market is in consolidation/confusion
    # If appropriate, place opposite trade
# else wait for a minute and try again
