"""
Day 3 - Beginner - Control Flow and Logical Operators

Program Descriptions:

Condition of the task:

"""
while True:
    while True:
        size = input("What size pizza do you want? S, M, or L\n: ").upper()
        if size.isalpha() and size == "S" or size == "M" or size == "L":
            break
    break

