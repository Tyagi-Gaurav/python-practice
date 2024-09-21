from datetime import datetime, timedelta
import pandas as pd
from mt5_client import display_data_frame, get_rates_using_bars
from sma import detect_crossover
from trade import place_buy_order, place_sell_order
from pytz import timezone
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
        from_local_cyp = datetime.now(cyprus_tz) - timedelta(hours=1)
        print(f"From: {from_local_cyp}\nTo: {to_local_cyp}\nSymbol: {symbol}")
        ticks_frame = get_rates_using_bars(symbol)
        # display_data_frame(ticks_frame)
        signal = detect_crossover(ticks_frame)
        if signal == "bullish":
            print("Placing Buy order now")
            print(f"local_now: {datetime.now()}: Buy Price: {ask_price}, Sell Price: {bid_price}")
            # Place Buy trade (If previous then close that)
            position_id = place_buy_order(symbol)
        elif signal == 'bearish':
            # Place Sell Trade (If previous then close that)
            print(f"Placing Sell order now with position_id {position_id}")
            print(f"local_now: {datetime.now()}: Buy Price: {ask_price}, Sell Price: {bid_price}")
            if position_id != -1:
                place_sell_order(symbol, position_id)
                position_id = -1
        time.sleep(60)
    mt5.shutdown()
    print("Program terminated...")


if __name__ == '__main__':
    main()
