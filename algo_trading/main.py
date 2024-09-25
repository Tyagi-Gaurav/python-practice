from datetime import datetime
import mt5_client
import sma
import trade
import time
import MetaTrader5


def save(df, position):
    df.to_csv(f"{position.order_ticket - datetime.now().timestamp()}.csv")


def start(symbol, end_time=60 * 60 * 12, interval_in_seconds=60):
    t_end = time.time() + end_time  # Run for 12 hour
    trades = trade.Trade()
    while time.time() < t_end:
        if trade.market_is_open():
            ask_price = MetaTrader5.symbol_info_tick(symbol).ask
            bid_price = MetaTrader5.symbol_info_tick(symbol).bid
            ticks_frame = mt5_client.get_rates_using_bars(symbol)
            (df, signal) = sma.detect_crossover(ticks_frame)
            if signal == "bullish":
                print("Placing Buy order now")
                print(f"local_now: {datetime.now()}: Buy Price: {ask_price}, Sell Price: {bid_price}")
                # Place Buy trade (If previous then close that)
                position = trade.place_buy_order(df, symbol)
                if position:
                    save(df, position)
                    trades.add_position(position)
            elif signal == 'bearish':
                # Place Sell Trade (If previous then close that)
                print("Market is Bearish")
                # print(f"local_now: {datetime.now()}: Buy Price: {ask_price}, Sell Price: {bid_price}")
                for position in trades.get_open_positions():
                    trade.place_sell_order(position)
            else:
                print("...")
        else:
            print(f"Market is closed. Trying again in {interval_in_seconds} seconds.")
        time.sleep(interval_in_seconds)


def main():
    start("XTIUSD")
    mt5.shutdown()
    print("Program terminated...")


if __name__ == '__main__':
    main()
