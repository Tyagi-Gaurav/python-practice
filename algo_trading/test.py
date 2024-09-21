import unittest
from unittest.mock import patch
import main
import pandas as pd


class TestStringMethods(unittest.TestCase):

    @patch('mt5_client.get_rates_using_bars')
    @patch('trade.place_buy_order')
    @patch('MetaTrader5.symbol_info_tick')
    def test_upper(self, symbol_info_mock, trade_buy_order, get_rates_using_bars_mock):
        get_rates_using_bars_mock.return_value  =  pd.read_csv("test/sma_20_crossover.csv")
        symbol_info_mock.return_value = type('',(object,),{"ask": 1, "bid" : 1})()
        main.start("XTI_USD", 1, 1)
        assert trade_buy_order.called



if __name__ == '__main__':
    unittest.main()