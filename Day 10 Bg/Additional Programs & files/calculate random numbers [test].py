"""
Day 10 - Beginner - Functions with Outputs

"""
import random


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
test_list = list(range(1, 30))

for oper in operations:
    operation_function = operations[oper]
    x = random.choice(test_list[10:])
    y = random.choice(test_list[:10])

    z = operation_function(x, y)

    z = round(z, 2)
    print(f"{x} {oper} {y} = {z}")
