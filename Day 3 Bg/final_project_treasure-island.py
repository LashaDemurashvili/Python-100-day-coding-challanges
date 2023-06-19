"""
Day 3 - Beginner - Control Flow and Logical Operators

Program Descriptions:
using if elif else statement for specific result.

Condition of the task:
see the dir ==> Conditions - Flow Charts/final project_treasure-island.png
"""

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n: ').lower()
if direction == "left":
    ask_1 = input('You\'ve come to a lake. There is an island in the middle of the lake. '
                  'Type "wait" to wait for a boat. Type "swim" to swim across.\n: ').lower()
    if ask_1 == "wait":
        ask_2 = input('You arrive at the island unharmed. There is a house with 3 doors. '
                      'One red, one yellow and one blue. Which colour do you choose?\n: ').lower()
        if ask_2 == "red":
            print("Burned by fire Game Over.")
        elif ask_2 == "yellow":
            print("You Win!")
        elif ask_2 == "Blue":
            print("Eaten by beasts Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attack by trout Game Over.")
else:
    print("Fall into a hole Game Over.")