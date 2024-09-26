from datetime import datetime

import MetaTrader5 as mt5
import logging
from position import Position
logger = logging.getLogger(__name__)

def market_is_open():
    result = mt5.symbol_info_tick("XTIUSD")._asdict()
    difference = datetime.now().timestamp() - result['time']
    # logging.info (f"timeNow {datetime.now().timestamp()} - tickTime: {result["time"]}, difference: {difference}")
    return difference < 10


def wwma(values, n):
    return values.ewm(alpha=1 / n, adjust=False).mean()


def atr(df, n=14):
    data = df.copy()
    high = data["high"]
    low = data["low"]
    close = data["close"]
    data['tr0'] = abs(high - low)
    data['tr1'] = abs(high - close.shift())
    data['tr2'] = abs(low - close.shift())
    tr = data[['tr0', 'tr1', 'tr2']].max(axis=1)
    return wwma(tr, n).iloc[-1]


def open_positions():
    positions_total = mt5.positions_total()
    logging.info(f"Number of open positions: {positions_total}")
    return positions_total > 0


def place_buy_order(df, symbol):
    lot = 1.0
    current_atr = atr(df)
    tp_atr_multiplier = 1.2
    sl_atr_multiplier = 1
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask
    logging.info(f"1. Placing order at point {point} with buy at {price} using atr {current_atr}")
    deviation = 20  # TODO What is this?
    sl = price - current_atr * sl_atr_multiplier
    tp = price + current_atr * tp_atr_multiplier
    logging.info(f"current_atr {current_atr}")
    request = {
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

    if not open_positions():
        result = mt5.order_send(request)
        logging.info("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol, lot, price, deviation))
        if result:
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                logging.info("2. order_send failed, retcode={}".format(result.retcode))
                # request the result as a dictionary and display it element by element
                result_dict = result._asdict()
                for field in result_dict.keys():
                    logging.info("{}={}".format(field, result_dict[field]))
                    # if this is a trading request structure, display it element by element as well
                    if field == "request":
                        traderequest_dict = result_dict[field]._asdict()
                        for tradereq_filed in traderequest_dict:
                            print("       traderequest: {}={}".format(tradereq_filed,
                                                                      traderequest_dict[tradereq_filed]))
                logging.info("shutdown() and quit")
            else:
                logging.info(result)
                logging.info(result.order)
                return Position(datetime.now(), symbol, result.ask, "BUY", result.volume, sl, tp,
                                result.order)
        else:
            logging.info("Could not place order. Please check order request.")
    else:
        logging.info("There are open buy order. Not placing order until they close.")


def place_sell_order(position):
    deviation = 20
    logging.info(f"PLacing sell order for position with ticket: {position.order_ticket}")
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": position.symbol,
        "volume": position.volume,
        "type": mt5.ORDER_TYPE_SELL,
        "position": position.order_ticket,
        "price": position.open_price,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script close",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    if market_is_open():
        # send a trading request
        result = mt5.order_send(request)
        # check the execution result
        logging.info(
            "3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position.order_ticket,
                                                                                           position.symbol,
                                                                                           position.volume,
                                                                                           position.open_price,
                                                                                           deviation));
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logging.info("4. order_send failed, retcode={}".format(result.retcode))
            logging.info("result comment: ", result.comment)
        else:
            logging.info("4. position #{} closed, {}".format(position.order_ticket, result))
            # request the result as a dictionary and display it element by element
            result_dict = result._asdict()
            for field in result_dict.keys():
                logging.info("{}={}".format(field, result_dict[field]))
                # if this is a trading request structure, display it element by element as well
                if field == "request":
                    traderequest_dict = result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        logging.info("traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
    else:
        logging.info("Not sending order. Market is closed.")
        return None


class Trade:
    def __init__(self):
        self.positions = []

    def add_position(self, position):
        self.positions.append(position)

    def get_open_positions(self):
        return [open_pos for open_pos in self.positions if open_pos.status == 'OPEN']
