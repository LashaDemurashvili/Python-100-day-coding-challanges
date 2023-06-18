"""
Day 3 - Beginner - Control Flow and Logical Operators

Program Descriptions:

Condition of the task:
see the flow chart in the dir ==> Conditions - Flow Charts/ride price.png
"""

height = float(input("Enter your height: "))

if height > 120:
    age = int(input("Enter your age: "))
    if age < 12:
        print("you can ride\nPrice is $5")
    elif age <= 18:
        print("you can ride\nPrice is $7")
    else:
        print("you can ride\nPrice is $12")
else:
    print("You can't ride")
