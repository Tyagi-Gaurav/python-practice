class Events:
    def __init__(self, events):
        self.events = events

    def __str__(self):
        return "events: {0} ".format(
            self.events
        )

    def __repr__(self):
        return self.__str__()


class Event:
    def __init__(self, event_name, odds):
        self.event_name = event_name
        self.odds = odds

    def __str__(self):
        return "event_name: {0}, " \
               "odds: {1} ".format(
            self.event_name,
            self.odds
        )

    def __repr__(self):
        return self.__str__()


class Odd:
    def __init__(self, name, f_odd):
        self.name = name
        self.f_odd = f_odd

    def __str__(self):
        return "name: {0},  " \
               "odd: {1}, ".format(
            self.name,
            self.f_odd
        )

    def __repr__(self):
        return self.__str__()