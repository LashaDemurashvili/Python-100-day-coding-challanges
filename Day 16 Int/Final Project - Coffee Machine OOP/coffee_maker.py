class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 500,
            "coffee": 200,
        }

    def report(self):
        """Prints a report of all resources."""
        """Make automation"""
        in_ml = ['water', 'milk']
        in_g = ['coffee']

        print("See the report")
        for key, value in self.resources.items():
            result = f"{key.ljust(10)} {value}"
            if key in in_ml:
                print(f"{result}ml")
            elif key in in_g:
                print(f"{result}g")
            else:
                print(f"{result}")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

