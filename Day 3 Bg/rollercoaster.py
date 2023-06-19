"""
Day 3 - Beginner - Control Flow and Logical Operators

Program Descriptions:

Condition of the task:
see the dir ==> Conditions - Flow Charts/rollercoaster.png
"""

print("Welcome to the roller coaster!")

# using while loop to avid any errors
while True:
    height = input("What is your height in cm?: ")
    if height.isdigit() and len(height) == 3:
        height = int(height)
        break

bill = 0

if height > 120:
    print("You can ride the rollercoaster!")

    # using while loop to avid any errors
    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            age = int(age)
            break

    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age < 18:
        print("Youth tickets are $7.")
        bill = 7
    elif 45 <= age <= 55:  # same as: age >= 45 and age <= 55
        print("Free ticket !")
        bill = 0
    else:
        print("Adult tickets are $12.")
        bill = 12

    print("Photo price is $3")

    # using while loop to avid any errors
    while True:
        wants_photo = input("Dou you want photo? Y / N: ").lower()
        if wants_photo == "y":
            bill += 3
            break
        elif wants_photo == "n":
            break

    print(f"The total bill is ${bill}")
else:
    print("You can't ride")
