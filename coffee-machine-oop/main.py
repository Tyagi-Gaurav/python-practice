from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker, Ingredient, Coffee

off_menu_item = MenuItem("of", "Switch off the machine")
report_menu_item = MenuItem("r", "Current resource status")
latte_menu_item = MenuItem("l", "Make Latte")
cappuccino_menu_item = MenuItem("c", "Make Cappuccino")
espresso_menu_item = MenuItem("e", "Make Espresso")

menu = Menu([off_menu_item, report_menu_item, latte_menu_item, cappuccino_menu_item, espresso_menu_item])

water = Ingredient("water", 100, "ml")
coffee = Ingredient("coffee", 500, "g")
milk = Ingredient("milk", 1000, "ml")

latte = Coffee("latte", {"water": 200, "milk": 200, "coffee": 50}, 1.50)
cappuccino = Coffee("cappuccino", {"water": 200, "milk": 100, "coffee": 100}, 2.50)
espresso = Coffee("espresso", {"water": 200, "coffee": 100}, 2.50)

coffees = {"l": latte, "c": cappuccino, "e": espresso}

coffee_maker = CoffeeMaker({"water": water, "coffee": coffee, "milk": milk})
money_machine = MoneyMachine()


def get_money():
    print("Please insert coins")
    q = int(input("How many quarters? "))
    d = int(input("How many dimes? "))
    n = int(input("How many nickels? "))
    p = int(input("How many pennies? "))
    return q, d, n, p


def print_report():
    print(coffee_maker.report())
    print(money_machine.report())


def prompt_user():
    return input("What would you like to do? : ")


while coffee_maker.is_on():
    print(menu)
    selected_option = prompt_user()

    if selected_option == "of":
        coffee_maker.turn_off()
    elif selected_option == "r":
        print_report()
    else:
        coffee = coffees[selected_option]
        if coffee_maker.can_make(coffee):
            print(f"Cost of drink: ${coffee.cost}.")
            quarters, dimes, nickels, pennies = get_money()
            total = money_machine.calculate_total(quarters, dimes, nickels, pennies)
            (change, is_success) = money_machine.take_payment(total, coffee.cost)
            if not is_success:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"You gave ${total / 100}. Here is ${change / 100} in change")
                coffee_maker.make(coffee)
