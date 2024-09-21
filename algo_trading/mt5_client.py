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

def get_rates_using_bars(symbol, number_of_bars=1000):
    # get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
    return mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M5, 0, number_of_bars)

def display_data_frame(ticks_frame):
    # convert time in seconds into the datetime format
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

    # display data
    # print("\nDisplay dataframe with ticks")
    print(ticks_frame)


def save_data_frame_to_csv(ticks, csv_file_name):
    ticks.to_csv(csv_file_name)
