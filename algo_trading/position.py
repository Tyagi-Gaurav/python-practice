
class Position:
    def __init__(self, open_datetime, symbol, open_price, order_type, volume, sl, tp, order_ticket, status="OPEN"):
        self.status = status
        self.symbol = symbol
        self.order_ticket = order_ticket
        self.tp = tp
        self.sl = sl
        self.volume = volume
        self.order_type = order_type
        self.open_price = open_price
        self.open_datetime = open_datetime
