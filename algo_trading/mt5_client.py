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


def get_rates(date_from, date_to, symbol, number_of_bars=10):
    # get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
    return mt5.copy_rates_range(symbol, mt5.TIMEFRAME_M5, date_from, date_to)


def display_data_frame(ticks_frame):
    # convert time in seconds into the datetime format
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

    # display data
    # print("\nDisplay dataframe with ticks")
    print(ticks_frame)


def save_data_frame_to_csv(ticks, csv_file_name):
    ticks.to_csv(csv_file_name)
