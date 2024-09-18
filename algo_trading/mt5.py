from datetime import datetime, timedelta
import time
import pandas as pd
from pytz import timezone
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


def get_rates(date_from, symbol, number_of_bars=10):
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


def detect_collision(df, colA, colB):
    df['sma_delta'] = df[colA] - df[colB]
    row = df[df.sma_delta == df.sma_delta.min()]
    if round(abs(row['sma_delta'].item()), 4) <= 0.001:
        print (f"{colA} going under {colB} at")
        print (row)
        return True
    return False


def main():
    t_end = time.time() + 60 * 60 #Run for 60 minutes
    while time.time() < t_end:
        cyprus_tz = timezone('Asia/Famagusta')
        local_cyp = datetime.now(cyprus_tz)
        local_now = datetime.now()
        # local_cyp = datetime(2024, 9, 18, 14, 35, 0)
        before_minutes = 10
        from_time = local_now - timedelta(minutes=before_minutes)
        symbol = "XTIUSD"
        # print(f"Cyprus: {local_cyp}\nNow: {local_now}\nFrom: {from_time}\nSymbol: {symbol}")
        ticks = get_rates(from_time, symbol, 120)
        # print (ticks)
        ticks_frame = pd.DataFrame(ticks)
        # display_data_frame(ticks_frame)
        ticks_frame = ticks_frame.drop(['spread', 'real_volume', 'tick_volume'], axis=1)
        ticks_frame = sma(20, ticks_frame, 'close')
        ticks_frame = sma(50, ticks_frame, 'close')
        if detect_collision(ticks_frame, 'SMA50', 'SMA20'):
            print ("Placing Buy order now")
            #Place Buy trade (If previous then close that)
            pass
        elif detect_collision(ticks_frame, 'SMA20', 'SMA50'):
            #Place Sell Trade (If previous then close that)
            print("Placing Sell order now")
            pass
        # save_data_frame_to_csv(ticks_frame, f"data-{str(time.time())}.csv")
        # display_data_frame(ticks_frame)
        time.sleep(5)
    mt5.shutdown()
    print ("Program terminated...")


if __name__ == '__main__':
    main()
