from datetime import datetime
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5

# connect to MetaTrader 5
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

# request connection status and parameters
print(mt5.terminal_info())
# get data on MetaTrader 5 version
print(mt5.version())

def main():
    print("Hello world")

# Returns time, bid, ask, last, flags
xtiusd_ticks = mt5.copy_ticks_range("XTIUSD", datetime(2024,8,29, 9), datetime(2024,8,29,10), mt5.COPY_TICKS_ALL)
print('xtiusd_ticks(', len(xtiusd_ticks), ')')
for val in xtiusd_ticks[:100]: print(val)

mt5.shutdown()
# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(xtiusd_ticks)
# convert time in seconds into the datetime format
ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

# display data
print("\nDisplay dataframe with ticks")
print(ticks_frame.head(10))

# Get Data every minute for the last minute in a loop

if __name__ == '__main__':
    main()