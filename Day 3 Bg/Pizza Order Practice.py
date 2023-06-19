"""
Day 3 - Beginner - Control Flow and Logical Operators

Program Descriptions: pizza order program

Condition of the task:

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1
"""

print("Welcome to Python Pizza Deliveries!")
bill = 0

while True:
    while True:
        size = input("What size pizza do you want? S, M, or L\n: ").upper()
        if size.isalpha() and size == "S" or size == "M" or size == "L":
            break

    while True:
        add_pepperoni = input("Do you want pepperoni? Y or N\n: ").upper()
        if add_pepperoni.isalpha() and add_pepperoni == "Y" or add_pepperoni == "N":
            break

    while True:
        extra_cheese = input("Do you want extra cheese? Y or N\n: ").upper()
        if extra_cheese.isalpha() and extra_cheese == "Y" or extra_cheese == "N":
            break

    break

# prices
Small_Pizza = 15
Medium_Pizza = 20
Large_Pizza = 25

Pepperoni_for_Small_Pizza = 2
Pepperoni_for_Medium_or_Large_Pizza = 3


Extra_cheese_for_any_size_pizza = 1

# option 1
"""
if size == "S":
    bill = Small_Pizza
    if add_pepperoni == "Y":
        bill += Pepperoni_for_Small_Pizza
    if extra_cheese == "Y":
        bill += Extra_cheese_for_any_size_pizza

elif size == "M":
    bill = Medium_Pizza
    if add_pepperoni == "Y":
        bill += Pepperoni_for_Medium_or_Large_Pizza
    if extra_cheese == "Y":
        bill += Extra_cheese_for_any_size_pizza

elif size == "L":
    bill = Large_Pizza
    if add_pepperoni == "Y":
        bill += Pepperoni_for_Medium_or_Large_Pizza
    if extra_cheese == "Y":
        bill += Extra_cheese_for_any_size_pizza

print(f"Your final bill is: ${bill}.")
"""

# option 2 this is better
bill_1 = 0

if size == "S":
    bill_1 += Small_Pizza
elif size == "M":
    bill_1 += Medium_Pizza
elif size == "L":
    bill_1 += Large_Pizza

if add_pepperoni == "Y":
    if size == "S":
        bill_1 += Pepperoni_for_Small_Pizza
    elif size == "M" or size == "L":
        bill_1 += Pepperoni_for_Medium_or_Large_Pizza

if extra_cheese == "Y":
    bill_1 += Extra_cheese_for_any_size_pizza

print(f"Your final bill is: ${bill_1}.")