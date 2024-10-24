import pandas as pd
import logging
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
import MetaTrader5 as mt5

logger = logging.getLogger(__name__)

# connect to MetaTrader 5
if not mt5.initialize():
    logging.info("initialize() failed")
    mt5.shutdown()

# request connection status and parameters
print(mt5.terminal_info())
# get data on MetaTrader 5 version
print(mt5.version())


def get_rates_using_bars(symbol, number_of_bars=1000):
    ticks = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M5, 0, number_of_bars)
    ticks_frame = pd.DataFrame(ticks)
    return ticks_frame.drop(['spread', 'real_volume', 'tick_volume'], axis=1)


def get_positions_total():
    return mt5.positions_total()


def get_symbol_info_tick(symbol):
    return mt5.symbol_info_tick(symbol)


def get_symbol_info(symbol):
    return mt5.symbol_info(symbol)


def display_data_frame(ticks_frame):
    # convert time in seconds into the datetime format
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')
    logging.debug(ticks_frame)


def save_data_frame_to_csv(ticks, csv_file_name):
    ticks.to_csv(csv_file_name)

def shutdown():
    mt5.shutdown()