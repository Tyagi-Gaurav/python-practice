from prettytable import PrettyTable


class MoneyMachine:
    def __init__(self):
        self.money = 0

    def take_payment(self, amount_paid, cost):
        cost_in_pennies = cost * 100
        if amount_paid > cost_in_pennies:
            self.money += cost_in_pennies
            return amount_paid - cost_in_pennies, True
        else:
            return 0, False

    def current_total(self):
        return self.money

    @staticmethod
    def calculate_total(q, d, n, p):
        return q * 25 + d * 10 + n * 5 + p

    def report(self):
        x = PrettyTable()

        x.add_column("Money", [self.money / 100])

        return x.get_string()
