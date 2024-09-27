import logging
from datetime import datetime

import MetaTrader5
import MetaTrader5 as mt5

import mt5_client
import sma
from position import Position

logger = logging.getLogger(__name__)


def is_market_open():
    result = mt5_client.get_symbol_info_tick("XTIUSD")._asdict()
    difference = datetime.now().timestamp() - result['time']
    logging.debug(f"timeNow {datetime.now().timestamp()} - tickTime: {result["time"]}, difference: {difference}")
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
    point = mt5_client.get_symbol_info(symbol).point
    price = mt5_client.get_symbol_info_tick(symbol).ask
    logging.info(f"Placing order at point {point} with buy at {price} using atr {current_atr}")
    deviation = 10
    sl = price - current_atr * sl_atr_multiplier
    tp = price + current_atr * tp_atr_multiplier
    logging.info(f"current_atr {current_atr}")
    request = create_buy_request_with(deviation, lot, price, sl, symbol, tp)

    if not open_positions():
        result = mt5.order_send(request)
        logging.debug(
            "order_send(): by {} {} lots at {} with deviation={} points".format(symbol, lot, price, deviation))
        if result:
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                handle_trade_failure(result)
            else:
                logging.info(result)
                return Position(datetime.now(), symbol, result.ask, "BUY", result.volume, sl, tp,
                                result.order)
        else:
            logging.info("Could not place order. Please check order request.")
    else:
        logging.info("There are open buy order. Not placing order until they close.")


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


def place_sell_order(position):
    deviation = 20
    logging.info(f"PLacing sell order for position with ticket: {position.order_ticket}")
    request = create_sell_request_with(deviation, position)
    if is_market_open():  # TODO check if position is still open
        result = mt5.order_send(request)
        logging.info(
            "close position #{}: sell {} {} lots at {} with deviation={} points".format(position.order_ticket,
                                                                                        position.symbol,
                                                                                        position.volume,
                                                                                        position.open_price,
                                                                                        deviation));
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logging.info("order_send failed, retcode={}".format(result.retcode))
            logging.info("result comment: ", result.comment)
        else:
            logging.info("position #{} closed, {}".format(position.order_ticket, result))
    else:
        logging.info("Not sending order. Market is closed.")
        return None


def create_sell_request_with(deviation, position):
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
    return request


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


def apply_sma_strategy(symbol):
    ask_price = mt5_client.get_symbol_info_tick(symbol).ask
    bid_price = mt5_client.get_symbol_info_tick(symbol).bid
    ticks_frame = mt5_client.get_rates_using_bars(symbol)
    if mt5_client.get_positions_total() == 0:
        (df, signal) = sma.detect_crossover(ticks_frame)
        if signal == "bullish":
            logger.info("Placing Buy order now")
            logger.info(f"local_now: {datetime.now()}: Buy Price: {ask_price}, Sell Price: {bid_price}")
            # Place Buy trade (If previous then close that)
            position = place_buy_order(df, symbol)
            if position:
                save(df, position)
                trades.add_position(position)
        elif signal == 'bearish':
            # Place Sell Trade (If previous then close that)
            logging.info("Market is Bearish")
            # logging.info(f"local_now: {datetime.now()}: Buy Price: {ask_price}, Sell Price: {bid_price}")
            for position in trades.get_open_positions():
                place_sell_order(position)
                position.status = 'CLOSED'
        else:
            logging.info("...")
    else:
        logging.info("There are some open positions.")
