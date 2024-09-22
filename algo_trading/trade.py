from datetime import datetime

import MetaTrader5 as mt5

def market_is_open():
    result = mt5.symbol_info_tick("XTIUSD")._asdict()
    difference = datetime.now().timestamp() - result['time']
    return difference < 10

def place_buy_order(symbol):
    lot = 1.0
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask
    print(f"1. Placing order at point {point} with buy at {price}")
    deviation = 20
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": price - 100 * point,
        "tp": price + 100 * point,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    if market_is_open():
        result = mt5.order_send(request)
        print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol, lot, price, deviation))
        print(result)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("2. order_send failed, retcode={}".format(result.retcode))
            # request the result as a dictionary and display it element by element
            result_dict = result._asdict()
            for field in result_dict.keys():
                print("   {}={}".format(field, result_dict[field]))
                # if this is a trading request structure, display it element by element as well
                if field == "request":
                    traderequest_dict = result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
            print("shutdown() and quit")
        else:
            return result.order
    else:
        print("Not sending order. Market is closed.")
        return None


def get_orders(ticket):
    order_for_ticket = mt5.orders_get(ticket)
    # order_for_ticket._asdiict().keys()

    # df = pd.DataFrame(list(gbp_orders), columns=gbp_orders[0]._asdict().keys())


def place_sell_order(symbol, order_ticket):
    lot = 1.0
    price = mt5.symbol_info_tick(symbol).bid
    deviation = 20
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_SELL,
        "position": order_ticket,
        "price": price,
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
            "3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id, symbol, lot, price,
                                                                                           deviation));
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("4. order_send failed, retcode={}".format(result.retcode))
            print("   result", result)
        else:
            print("4. position #{} closed, {}".format(position_id, result))
            # request the result as a dictionary and display it element by element
            result_dict = result._asdict()
            for field in result_dict.keys():
                print("   {}={}".format(field, result_dict[field]))
                # if this is a trading request structure, display it element by element as well
                if field == "request":
                    traderequest_dict = result_dict[field]._asdict()
                    for tradereq_filed in traderequest_dict:
                        print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
    else:
        print ("Not sending order. Market is closed.")
        return None
