from data import menu

start = " Welcome to coffee machine ".center(55, "*")
print(start)

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def report():
    """print resources"""
    print("Here is current resources report")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {profit}")


def is_resources_sufficient(order_ingredients):
    """"check if resources is enough"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """return received total money"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """return True if payment accepted or False if denied"""
    """We need profit to be Global variable, for modify"""
    if money_received >= drink_cost:
        if money_received > drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """update resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}️. Enjoy!")


print("Type 'report' if you want to see resources"
      "\nType 'off' if you want to off machine")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        print("Process was ended")
        is_on = False
    elif choice == "report":
        report()
    else:
        drink = menu[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])





