import data

machine_state = "on"


def prompt_user():
    return input("What would you like? (espresso/latte/cappuccino): ")


def print_report():
    print(f"Water: {data.resources['water']}ml")
    print(f"Milk: {data.resources['milk']}ml")
    print(f"Coffee: {data.resources['coffee']}g")
    print(f"Money: ${data.resources['money'] / 100}")


def valid(drink):
    return drink == "espresso" or drink == "latte" or drink == "cappuccino"


def get_money():
    print("Please insert coins")
    q = int(input("How many quarters? "))
    d = int(input("How many dimes? "))
    n = int(input("How many nickels? "))
    p = int(input("How many pennies? "))
    return q, d, n, p


def cost_of(drink):
    return data.MENU[drink]["cost"]


def calculate_total(q, d, n, p):
    return q * 25 + d * 10 + n * 5 + p


def check_transaction_is_successful(drink, total):
    return cost_of(drink) * 100 <= total


def make(drink):
    needed_water = data.MENU[drink]["ingredients"]["water"]
    needed_coffee = data.MENU[drink]["ingredients"]["coffee"]
    needed_milk = 0

    if drink == "cappucino" or drink == "latte":
        needed_milk = data.MENU[drink]["ingredients"]["milk"]

    data.resources["water"] -= needed_water
    data.resources["coffee"] -= needed_coffee
    data.resources["milk"] -= needed_milk


def resources_available_for(drink):
    needed_water = data.MENU[drink]["ingredients"]["water"]
    needed_coffee = data.MENU[drink]["ingredients"]["coffee"]
    needed_milk = 0

    if drink == "cappucino" or drink == "latte":
        needed_milk = data.MENU[drink]["ingredients"]["milk"]

    available_water = data.resources["water"]
    available_coffee = data.resources["coffee"]
    available_milk = data.resources["milk"]

    if needed_water > available_water:
        print("Sorry there is not enough water.")
        return False
    elif needed_milk > available_milk:
        print("Sorry there is not enough milk.")
        return False
    elif needed_coffee > available_coffee:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


while machine_state == "on":
    user_drink = prompt_user()

    if user_drink == "off":
        machine_state = "off"
    elif user_drink == "report":
        print_report()
    elif valid(user_drink):
        if resources_available_for(user_drink):
            print(f"Cost of drink: ${cost_of(user_drink)}.")
            quarters, dimes, nickels, pennies = get_money()
            total = calculate_total(quarters, dimes, nickels, pennies)
            if check_transaction_is_successful(user_drink, total):
                drink_cost_in_pennies = cost_of(user_drink) * 100
                change = total - drink_cost_in_pennies
                data.resources["money"] += drink_cost_in_pennies
                print(f"You gave ${total / 100}. Here is ${change / 100} in change")
                make(user_drink)
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Could not understand input. Please try again.")
