import logging
from datetime import datetime

import MetaTrader5 as mt5

import mt5_client
import sma
from Domain import Given
from position import Position
from risk import Risk

logger = logging.getLogger(__name__)


def is_market_open():
    result = mt5_client.get_symbol_info_tick("XTIUSD")._asdict()
    difference = datetime.now().timestamp() - result['time']
    logging.debug(f"timeNow {datetime.now().timestamp()} - tickTime: {result["time"]}, difference: {difference}")
    return difference < 10


def wwma(values, n):
    return values.ewm(alpha=1 / n, adjust=False).mean()


def atr(given: Given, n=14):
    df = given.__dict__.get("df")
    data = df.copy()
    high = data["high"]
    low = data["low"]
    close = data["close"]
    data['tr0'] = abs(high - low)
    data['tr1'] = abs(high - close.shift())
    data['tr2'] = abs(low - close.shift())
    tr = data[['tr0', 'tr1', 'tr2']].max(axis=1)
    atr_value = wwma(tr, n).iloc[-1]
    print(f"Adding ATR {atr_value}")
    given.add("atr", atr_value)
    return atr_value


def no_open_positions(_):
    positions_total = mt5.positions_total()
    logging.info(f"Number of open positions: {positions_total}")
    return positions_total == 0


def place_sell_order(given: Given, risk: Risk, symbol: str):
    lot = 1.0
    current_atr = given.__dict__.get("atr")

    tp_atr_multiplier = risk.get_tp_atr_multiplier()
    sl_atr_multiplier = 1
    price = mt5_client.get_symbol_info_tick(symbol).ask
    logging.info(f"Placing SELL order at {price} using atr {current_atr}")
    deviation = 10
    consolidation_range = given.__dict__.get("consolidation_range")
    price = price + consolidation_range
    sl = price + current_atr * sl_atr_multiplier
    tp = price - current_atr * tp_atr_multiplier
    logging.info(f"current_atr {current_atr}")
    send_order_and_handle_failure(create_sell_request_with(deviation, lot, price, sl, symbol, tp))


def send_order_and_handle_failure(request):
    result = mt5.order_send(request)
    # logging.debug(
    #     "order_send(): by {} {} lots at {} with deviation={} points".format(request.symbol,
    #                                                                         request.volume,
    #                                                                         request.price,
    #                                                                         request.deviation))
    if result:
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            handle_trade_failure(result)
        else:
            logging.info(result)
            # return Position(datetime.now(), request.symbol, result.ask, "BUY", result.volume, sl, tp,
            #                 result.order)
    else:
        logging.info("Could not place order. Please check order request.")


def create_buy_request_with(deviation, lot, price, sl, symbol, tp):
    return {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }


def create_sell_request_with(deviation, lot, price, sl, symbol, tp):
    return {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }


def handle_trade_failure(result):
    logging.info("order_send failed, retcode={}".format(result.retcode))
    # request the result as a dictionary and display it element by element
    result_dict = result._asdict()
    for field in result_dict.keys():
        logging.debug("{}={}".format(field, result_dict[field]))
        # if this is a trading request structure, display it element by element as well
        if field == "request":
            traderequest_dict = result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                logging.debug("traderequest: {}={}".format(tradereq_filed,
                                                           traderequest_dict[tradereq_filed]))


def save(df, position):
    df.to_csv(f"{position.order_ticket} - {datetime.now().timestamp()}.csv")


class Trade:
    def __init__(self):
        self.positions = []

    def add_position(self, position):
        self.positions.append(position)

    def get_open_positions(self):
        return [open_pos for open_pos in self.positions if open_pos.status == 'OPEN']


trades = Trade()


def place_buy_order(given: Given, risk: Risk, symbol):
    lot = 1.0
    current_atr = given.__dict__.get("atr")
    tp_atr_multiplier = risk.get_tp_atr_multiplier()
    sl_atr_multiplier = 1
    price = mt5_client.get_symbol_info_tick(symbol).ask
    logging.info(f"Placing BUY order at {price} using atr {current_atr}")
    deviation = 10
    consolidation_range = given.__dict__.get("consolidation_range")
    price = price - consolidation_range
    sl = price - current_atr * sl_atr_multiplier
    tp = price + current_atr * tp_atr_multiplier
    logging.info(f"current_atr {current_atr}")
    send_order_and_handle_failure(create_buy_request_with(deviation, lot, price, sl, symbol, tp))
