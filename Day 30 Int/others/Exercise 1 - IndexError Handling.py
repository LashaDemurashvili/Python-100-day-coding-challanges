import random

fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


x = random.randint(0, 5)
print("NO" if x >= 3 else "Yes", x)

make_pie(x)
