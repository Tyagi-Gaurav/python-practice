from datetime import datetime, timedelta
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


def get_data_from_mt5(from_time, to_time, symbol="EURUSD"):
    # Returns time, bid, ask, last, flags
    ticks = mt5.copy_ticks_range(symbol, from_time, to_time, mt5.COPY_TICKS_ALL)
    mt5.shutdown()  # TODO execute this before terminating the script
    return ticks


def display_data_frame(ticks):
    # create DataFrame out of the obtained data
    ticks_frame = pd.DataFrame(ticks)
    # convert time in seconds into the datetime format
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

    # display data
    print("\nDisplay dataframe with ticks")
    print(ticks_frame.head(10))


def main():
    to_time = datetime(2024, 9, 6, 17, 00)
    # to_time = datetime.now()
    from_time = to_time - timedelta(minutes=10)
    symbol = "EURUSD"
    print(f"Now: {to_time}, From Time: {from_time}, Symbol: {symbol}")
    ticks = get_data_from_mt5(from_time, to_time, symbol)
    display_data_frame(ticks)


if __name__ == '__main__':
    main()
