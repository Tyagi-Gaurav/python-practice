from datetime import datetime, timedelta
import mt5_client
import sma
import trade
import time
import MetaTrader5


def start(symbol, end_time=60 * 60 * 12, interval_in_seconds=60):
    t_end = time.time() + end_time  # Run for 12 hour
    order_ticket = -1
    while time.time() < t_end:
        ask_price = MetaTrader5.symbol_info_tick(symbol).ask
        bid_price = MetaTrader5.symbol_info_tick(symbol).bid
        ticks_frame = mt5_client.get_rates_using_bars(symbol)
        (df, signal) = sma.detect_crossover(ticks_frame)
        if signal == "bullish":
            print("Placing Buy order now")
            print(f"local_now: {datetime.now()}: Buy Price: {ask_price}, Sell Price: {bid_price}")
            # Place Buy trade (If previous then close that)
            order_ticket = trade.place_buy_order(df, symbol)
        elif signal == 'bearish':
            # Place Sell Trade (If previous then close that)
            # print(f"local_now: {datetime.now()}: Buy Price: {ask_price}, Sell Price: {bid_price}")
            if order_ticket != -1:
                print(f"Placing Sell order now with ticket {order_ticket}")
                trade.place_sell_order(df, symbol, order_ticket)
                order_ticket = -1
        else:
            print ("No signal")
        time.sleep(interval_in_seconds)


def main():
    start("XTIUSD")
    mt5.shutdown()
    print("Program terminated...")


if __name__ == '__main__':
    main()
