from datetime import datetime, timedelta

from algo_trading.mt5_client import get_rates, display_data_frame
from algo_trading.sma import sma, detect_crossover
from algo_trading.trade import place_buy_order, place_sell_order
from pytz import timezone
import pandas as pd
import time
import MetaTrader5 as mt5


def main():
    t_end = time.time() + 60 * 60 * 12  # Run for 12 hour
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
        ticks_frame = ticks_frame.drop(['spread', 'real_volume', 'tick_volume'], axis=1)
        # display_data_frame(ticks_frame)
        ticks_frame = sma(20, ticks_frame, 'close')
        ticks_frame = sma(50, ticks_frame, 'close')
        if detect_crossover(ticks_frame, 'SMA50', 'SMA20'):
            print("Placing Buy order now")
            print(f"local_now: {local_now}: Buy Price: {ask_price}, Sell Price: {bid_price}")
            # Place Buy trade (If previous then close that)
            position_id = place_buy_order(symbol)
        elif detect_crossover(ticks_frame, 'SMA20', 'SMA50'):
            # Place Sell Trade (If previous then close that)
            print(f"Placing Sell order now with position_id {position_id}")
            print(f"local_now: {local_now}: Buy Price: {ask_price}, Sell Price: {bid_price}")
            if position_id != -1:
                place_sell_order(symbol, position_id)
                position_id = -1
        else:
            print(f"{datetime.now()} - No collision detected\n")
        # save_data_frame_to_csv(ticks_frame, f"data-{str(time.time())}.csv")
        # display_data_frame(ticks_frame)
        time.sleep(60)
    mt5.shutdown()
    print("Program terminated...")


if __name__ == '__main__':
    main()
