"""
Day 15 - Intermediate - Local Development Environment Setup & the Coffee Machine

Coffee Machine Program
"""
import colorama as cl
from colorama import Fore, Back

from Resources.data import MENU as menu

cl.init(autoreset=True)

start = " Welcome to coffee machine "
print(Fore.YELLOW + start.center(len(start) * 2, "*").title())

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def prices(menu_dict: dict):
    print("\n")
    print(f"{Fore.BLUE}See coffee prices!")
    for item in menu_dict:
        coffee_name = item
        coffee_cost = menu_dict[item]["cost"]
        print(f"{coffee_name} - Price: ${coffee_cost}")


def report():
    """print resources"""
    print("\n")
    print("Here is current resources report")
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f"Money: ${profit}")


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    """We need profit to be Global variable, for modify"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


print("Type 'report' if you want to see resources"
      "\nType 'off' if you want to off machine")

# print prices
prices(menu_dict=menu)

is_on = True

while is_on:
    try:
        print("\n")
        prompt = input("What would you like? (espresso/latte/cappuccino): ")
        if prompt == "off":
            print(f"{Fore.RED}Process was ended !")
            is_on = False
        elif prompt == "report":
            report()
        else:
            drink = menu[prompt]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(prompt, drink["ingredients"])
    except:
        print(f"{Fore.RED} ERROR occur !!! \n Program restarted")
        continue
