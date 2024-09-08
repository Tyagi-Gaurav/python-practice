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


def get_ticks_range_from_mt5(from_time, to_time, ):
    # Returns time, bid, ask, last, flags
    return mt5.copy_ticks_range(symbol, from_time, to_time, mt5.COPY_TICKS_INFO)


def get_rates(date_from, symbol="EURUSD", number_of_bars=10):
    # get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
    return mt5.copy_rates_from(symbol, mt5.TIMEFRAME_M5, date_from, number_of_bars)


def display_data_frame(ticks_frame):
    # convert time in seconds into the datetime format
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

    # display data
    print("\nDisplay dataframe with ticks")
    print(ticks_frame.head(10))


def save_data_frame_to_csv(ticks, csv_file_name):
    ticks.to_csv(csv_file_name)


def sma(window_size, ticks_frame, column):
    ticks_frame[f'SMA{window_size}'] = ticks_frame[column].rolling(window_size).mean()
    # Drop null values
    ticks_frame.dropna(inplace=True)
    return ticks_frame


def main():
    to_time = datetime(2024, 9, 6, 23, 40)
    # to_time = datetime.now()
    from_time = to_time - timedelta(minutes=10)
    symbol = "EURUSD"
    print(f"Now: {to_time}, From Time: {from_time}, Symbol: {symbol}")
    ticks = get_rates(from_time, symbol, 120)
    ticks_frame = pd.DataFrame(ticks)
    ticks_frame = ticks_frame.drop(['spread', 'real_volume', 'tick_volume'], axis=1)
    ticks_frame_20 = sma(20, ticks_frame, 'close')
    ticks_frame_50 = sma(50, ticks_frame_20, 'close')
    display_data_frame(ticks_frame_50)
    save_data_frame_to_csv(ticks_frame_50, f"data-{str(time.time())}.csv")
    mt5.shutdown()


if __name__ == '__main__':
    main()
