class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, date_from, date_to, to_city, max_price, adults=2, kids=2):
        self.from_city = "LON"
        self.to_city = to_city
        self.date_from = date_from
        self.date_to = date_to
        self.adults = adults
        self.kids = kids
        self.cabin = "M"
        self.curr = "GBP"
        self.locale = "en"
        self.max_price = max_price

