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


def get_rates(date_from, date_to, symbol, number_of_bars=10):
    # get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
    return mt5.copy_rates_range(symbol, mt5.TIMEFRAME_M5, date_from, date_to)


def display_data_frame(ticks_frame):
    # convert time in seconds into the datetime format
    ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

    # display data
    print("\nDisplay dataframe with ticks")
    print(ticks_frame.tail(1))


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
    if round(abs(row['sma_delta'].item()), 4) <= 0.0001:
        print (f"{colA} going under {colB} at")
        print (row)
        return True
    return False

def place_buy_order(symbol):
    lot = 1.0
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask
    print(f"1. Placing order at point {point} with buy at {price}")
    deviation = 20
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": price - 100 * point,
        "tp": price + 100 * point,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(request)
    print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol, lot, price, deviation))
    print (result)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("2. order_send failed, retcode={}".format(result.retcode))
        # request the result as a dictionary and display it element by element
        result_dict = result._asdict()
        for field in result_dict.keys():
            print("   {}={}".format(field, result_dict[field]))
            # if this is a trading request structure, display it element by element as well
            if field == "request":
                traderequest_dict = result_dict[field]._asdict()
                for tradereq_filed in traderequest_dict:
                    print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
        print("shutdown() and quit")
    else:
        return result.order

def place_sell_order(symbol, position_id):
    lot = 1.0
    price = mt5.symbol_info_tick(symbol).bid
    deviation = 20
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL,
        "position": position_id,
        "price": price,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script close",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    # send a trading request
    result = mt5.order_send(request)
    # check the execution result
    print(
        "3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id, symbol, lot, price,
                                                                                       deviation));
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print("4. order_send failed, retcode={}".format(result.retcode))
        print("   result", result)
    else:
        print("4. position #{} closed, {}".format(position_id, result))
        # request the result as a dictionary and display it element by element
        result_dict = result._asdict()
        for field in result_dict.keys():
            print("   {}={}".format(field, result_dict[field]))
            # if this is a trading request structure, display it element by element as well
            if field == "request":
                traderequest_dict = result_dict[field]._asdict()
                for tradereq_filed in traderequest_dict:
                    print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))

def main():
    t_end = time.time() + 60 * 60 * 12 #Run for 12 hour
    position_id = -1
    symbol = "XTIUSD"
    while time.time() < t_end:
        ask_price = mt5.symbol_info_tick(symbol).ask
        bid_price = mt5.symbol_info_tick(symbol).bid
        cyprus_tz = timezone('Asia/Famagusta')
        to_local_cyp = datetime.now(cyprus_tz)
        from_local_cyp = datetime.now(cyprus_tz) - timedelta(hours=6)
        print(f"From: {from_local_cyp}\nTo: {to_local_cyp}\nSymbol: {symbol}")
        ticks = get_rates(from_local_cyp, to_local_cyp, symbol)
        ticks_frame = pd.DataFrame(ticks)
        # display_data_frame(ticks_frame)
        ticks_frame = ticks_frame.drop(['spread', 'real_volume', 'tick_volume'], axis=1)
        ticks_frame = sma(20, ticks_frame, 'close')
        ticks_frame = sma(50, ticks_frame, 'close')
        if detect_collision(ticks_frame, 'SMA50', 'SMA20'):
            print ("Placing Buy order now")
            print(f"local_now: {local_now}: Buy Price: {ask_price}, Sell Price: {bid_price}")
            #Place Buy trade (If previous then close that)
            position_id = place_buy_order(symbol)
        elif detect_collision(ticks_frame, 'SMA20', 'SMA50'):
            #Place Sell Trade (If previous then close that)
            print(f"Placing Sell order now with position_id {position_id}")
            print(f"local_now: {local_now}: Buy Price: {ask_price}, Sell Price: {bid_price}")
            if position_id != -1:
                place_sell_order(symbol, position_id)
                position_id = -1
        else:
            print (f"{datetime.now()} - No collision detected\n")
        # save_data_frame_to_csv(ticks_frame, f"data-{str(time.time())}.csv")
        # display_data_frame(ticks_frame)
        time.sleep(60)
    mt5.shutdown()
    print ("Program terminated...")


if __name__ == '__main__':
    main()
