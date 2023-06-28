"""
Day 13 - Beginner - Debugging How to Find and Fix Errors in your Code

# Debugging Leap Year
"""

# we need to convert into integer
year = int(input("Which year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
