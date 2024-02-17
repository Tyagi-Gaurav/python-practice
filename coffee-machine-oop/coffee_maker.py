from prettytable import PrettyTable


class CoffeeMaker:
    def __init__(self, resources):
        self.resources = resources
        self.on_state = True

    def is_on(self):
        return self.on_state

    def turn_off(self):
        self.on_state = False

    def report(self):
        x = PrettyTable()

        x.field_names = ["Resource", "status"]
        for key in self.resources:
            x.add_row([key, self.resources[key]])

        return x.get_string()

    def can_make(self, coffee):
        for key in coffee.ingredients:
            ingredient_amount = coffee.ingredients[key]
            resource = self.resources[key]
            if resource.amount < ingredient_amount:
                print(f"Sorry there is not enough {key}.")
                return False

        return True

    def make(self, coffee):
        for key in coffee.ingredients:
            ingredient_amount = coffee.ingredients[key]
            resource = self.resources[key]
            resource.amount -= ingredient_amount


class Coffee:
    def __init__(self, name, ingredients, cost):
        """

        :type cost: float
        :type ingredients: Map[String, Ingredient]
        :type name: string
        """
        self.cost = cost
        self.name = name
        self.ingredients = ingredients


class Ingredient:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit

    def __str__(self):
        return f"{self.amount}{self.unit}"
