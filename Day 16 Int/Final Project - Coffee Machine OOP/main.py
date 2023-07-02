from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

print("Type: \n'off' for stop process\n'Report' for report\nCoffee name for coffee")
while True:
    try:
        options = menu.get_items()
        choice = input(f"What would you like? {options}")
        if choice == 'off':
            print("Machine off")
            break
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    except Exception as e:
        print(f"There is some ERROR ==> {e}")
        print("Program Restarted !!!\n")
        continue


"""
# Create objects
# () for execute
# Object = ClassBlueprint()
# car = CarBlueprint() - for example
"""