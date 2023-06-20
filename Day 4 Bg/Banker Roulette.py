"""
Day 4 - Beginner - Randomisation and Python Lists


practice random module
practice split module

Condition of the task:
who will pay
"""
import random

names = input("Give me everybody's names, separated by a comma. \n: ")
spl_names = names.split(",")


# result =f split is lsit
# default split sep is - spaces " "

num_items = len(spl_names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = spl_names[random_choice]

print(f">> {person_who_will_pay} << is going to buy the meal today!")
