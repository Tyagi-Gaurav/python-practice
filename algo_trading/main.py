import logging
import time
from typing import List

import mt5_client
from Domain import Strategy, Rule, Task, When, do_nothing, Then, Given
from config import allowed_sell_trading, allowed_buy_trading
from risk import Risk
from sma import calculate_sma, detect_crossover, in_consolidation, is_bearish_crossover, calculate_consolidation_range, \
    is_bullish_crossover
from trade import place_sell_order, atr, no_open_positions, place_buy_order

logger = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')


# def start(symbol, end_time=60 * 60 * 12, interval_in_seconds=60):
#     t_end = time.time() + end_time  # Run for 12 hour
#     while time.time() < t_end:
#         if trade.is_market_open():
#             trade.apply_sma_strategy(symbol)
#         else:
#             logging.info(f"Market is closed. Trying again in {interval_in_seconds} seconds.")
#         time.sleep(interval_in_seconds)

class Trading:
    def __init__(self, symbol: str, strategies: List[Strategy]):
        self.strategies = strategies
        self.symbol = symbol

    def _get_data(self):
        return mt5_client.get_rates_using_bars(self.symbol)

    def start(self):
        end_time = 60 * 60 * 12
        interval_in_seconds = 60
        t_end = time.time() + end_time  # Run for 12 hour
        while time.time() < t_end:
            raw_data_frame = self._get_data()
            for strategy in self.strategies:
                strategy.apply(Given(df=raw_data_frame))
            # if trade.is_market_open():
            #     trade.apply_sma_strategy(symbol)
            # else:
            #     logging.info(f"Market is closed. Trying again in {interval_in_seconds} seconds.")
            time.sleep(interval_in_seconds)


def main():
    sma_strategy = Strategy("SMA Crossover",
                            [
                                Task("Calculate SMA 20", calculate_sma, sma_name="fast_sma", period=20),
                                Task("Calculate SMA 50", calculate_sma, sma_name="slow_sma", period=50),
                                Task("Detect crossover", detect_crossover, fast_sma="fast_sma", slow_sma="slow_sma")
                            ],
                            [
                                Rule(when=[When("If market in consolidation", in_consolidation)], then=[do_nothing]),
                                Rule(when=[When("Is Bearish crossover", is_bearish_crossover),
                                           When("Allowed Sell Trading", allowed_sell_trading),
                                           When("No Open Positions", no_open_positions)],
                                     then=[
                                         Then("Calculate ATR", atr),
                                         Then("Calculate Consolidation Range", calculate_consolidation_range),
                                         Then("Place Sell Order", place_sell_order, risk=Risk(), symbol="XTIUSD")
                                     ]),
                                Rule(when=[When("Is Bullish crossover", is_bullish_crossover),
                                           When("Allowed Buy Trading", allowed_buy_trading),
                                           When("No Open Positions", no_open_positions)],
                                     then=[
                                         Then("Calculate ATR", atr),
                                         Then("Calculate Consolidation Range", calculate_consolidation_range),
                                         Then("Place Buy Order", place_buy_order, risk=Risk(), symbol="XTIUSD")
                                     ])
                            ])

    trade1 = Trading("XTIUSD", [sma_strategy])
    trade1.start()
    mt5_client.shutdown()
    logging.info("Program terminated...")


if __name__ == '__main__':
    main()

#
# 0. Strategy Module
# 1. BackTesting Module
# 2. Risk Management module
# 3. Trade module
# 4. Unit testing
# 5. For every instrument,
##
