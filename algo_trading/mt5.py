from datetime import datetime, timedelta
import time
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


def display_data_frame(ticks_frame):
    # convert time in seconds into the datetime format
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

    # display data
    print("\nDisplay dataframe with ticks")
    print(ticks_frame.head(10))


def save_data_frame_to_csv(ticks, csv_file_name):
    ticks.to_csv(csv_file_name)


def sma(window_size, ticks_frame):
    ticks_frame[f'SMA{window_size}'] = ticks_frame['bid'].rolling(window_size).mean()
    # Drop null values
    ticks_frame.dropna(inplace=True)
    return ticks_frame


def main():
    to_time = datetime(2024, 9, 6, 17, 00)
    # to_time = datetime.now()
    from_time = to_time - timedelta(minutes=10)
    symbol = "EURUSD"
    print(f"Now: {to_time}, From Time: {from_time}, Symbol: {symbol}")
    ticks = get_data_from_mt5(from_time, to_time, symbol)
    ticks_frame = pd.DataFrame(ticks)
    ticks_frame = ticks_frame.drop(['flags','volume_real','volume','time_msc','last'], axis=1)
    ticks_frame = sma(20, ticks_frame)
    ticks_frame = sma(50, ticks_frame)
    display_data_frame(ticks_frame)
    save_data_frame_to_csv(ticks_frame, f"data-{str(time.time())}.csv")


if __name__ == '__main__':
    main()
