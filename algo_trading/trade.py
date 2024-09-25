from datetime import datetime

import MetaTrader5 as mt5

from position import Position


def market_is_open():
    result = mt5.symbol_info_tick("XTIUSD")._asdict()
    difference = datetime.now().timestamp() - result['time']
    # print (f"timeNow {datetime.now().timestamp()} - tickTime: {result["time"]}, difference: {difference}")
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
    print(f"Number of open positions: {positions_total}")
    return positions_total > 0


def place_buy_order(df, symbol):
    lot = 1.0
    current_atr = atr(df)
    tp_atr_multiplier = 1.4
    sl_atr_multiplier = 1
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask
    print(f"1. Placing order at point {point} with buy at {price} using atr {current_atr}")
    deviation = 20  # TODO What is this?
    sl = price - current_atr * sl_atr_multiplier
    tp = price + current_atr * tp_atr_multiplier
    print(f"current_atr {current_atr}")
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
        print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol, lot, price, deviation))
        if result:
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                print("2. order_send failed, retcode={}".format(result.retcode))
                # request the result as a dictionary and display it element by element
                result_dict = result._asdict()
                for field in result_dict.keys():
                    print("{}={}".format(field, result_dict[field]))
                    # if this is a trading request structure, display it element by element as well
                    if field == "request":
                        traderequest_dict = result_dict[field]._asdict()
                        for tradereq_filed in traderequest_dict:
                            print("       traderequest: {}={}".format(tradereq_filed,
                                                                      traderequest_dict[tradereq_filed]))
                print("shutdown() and quit")
            else:
                print(result)
                return Position(datetime.now(), symbol, result.ask, "BUY", result.volume, sl, tp,
                                result.order)
        else:
            print("Could not place order. Please check order request.")
    else:
        print("There are open buy order. Not placing order until they close.")


def place_sell_order(position):
    price = mt5.symbol_info_tick(position.symbol).bid
    deviation = 20
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
        print(
            "3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position.order_ticket,
                                                                                           position.symbol,
                                                                                           position.volume,
                                                                                           position.open_price,
                                                                                           deviation));
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("4. order_send failed, retcode={}".format(result.retcode))
            print("result", result)
        else:
            print("4. position #{} closed, {}".format(position.order_ticket, result))
            # request the result as a dictionary and display it element by element
            result_dict = result._asdict()
            for field in result_dict.keys():
                print("   {}={}".format(field, result_dict[field]))
                # if this is a trading request structure, display it element by element as well
                if field == "request":
                    traderequest_dict = result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
    else:
        print("Not sending order. Market is closed.")
        return None


class Trade:
    def __init__(self):
        self.positions = []

    def add_position(self, position):
        self.positions.append(position)

    def get_open_positions(self):
        return [open_pos for open_pos in self.positions if open_pos.status == 'OPEN']
