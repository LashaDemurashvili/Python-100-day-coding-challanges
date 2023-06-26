"""
Day 10 - Beginner - Functions with Outputs

Final Project: Calculator
"""
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

# calculation history save in list
calculation_history = []


def calculator():
    print(logo)

    try:
        num1 = float(input("What's the first number?: "))

        for symbol in operations:
            print(symbol)
        should_continue = True

        while should_continue:
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What's the next number?: "))

            if operation_symbol in operations:
                # after this code 'calculation_function' will be function, which is declared in 'operations' dictionary
                calculation_function = operations[operation_symbol]

                answer = calculation_function(num1, num2)
                answer = round(answer, 2)
                result = f"{num1} {operation_symbol} {num2} = {answer}"
                print(result)

                # add new calculation in 'calculation_history' list
                calculation_history.append(str(result))
            else:
                print("Wrong symbol !!!\n")
                continue

            ask_0 = input(
                f"Type 'y' to continue calculating with result {answer}, or type 'n' to start a new calculation, "
                "or 'q' to end the process: ")
            if ask_0 == "y":
                num1 = answer
            elif ask_0 == "n":
                # interrupt while loop
                should_continue = False

                # and call again calculator function
                calculator()
            else:
                print("Calculation process was ended !")
                should_continue = False
                # or we can use just - beak
                # break

    except Exception as ex:
        print("\n")
        print(f"Errors occur >>> {ex} !!!")
        print("Program Restart !")

        # call again calculator function
        calculator()


# launch
calculator()

print('\n', 'Calculation history')
print(calculation_history)
