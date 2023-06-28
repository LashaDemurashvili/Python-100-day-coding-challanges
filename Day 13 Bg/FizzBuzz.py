"""
Day 13 - Beginner - Debugging How to Find and Fix Errors in your Code

# Debugging FizzBuzz
"""

# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])


for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:  # and operator
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)  # no square brakes
