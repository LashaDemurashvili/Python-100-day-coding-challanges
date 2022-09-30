from recources.art import logo


# created functions which put into dictionary named - operations
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        ask_0 = input(f"Type 'y' to continue calculating with result {answer}, or type 'n' to start a new calculation, "
                      "or 'exit' to end the process: ")
        if ask_0 == "y":
            num1 = answer
        elif ask_0 == "n":
            should_continue = False
            calculator()
        else:
            print("Calculation process was ended")
            break


calculator()

