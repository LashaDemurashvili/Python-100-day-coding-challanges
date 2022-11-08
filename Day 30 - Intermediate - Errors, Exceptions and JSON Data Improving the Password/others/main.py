# add random numbers range to data.txt
from random import randint

with open("data.txt", "a") as dataFile:
    random_number = randint(1, 30)
    for i in range(random_number):
        file = dataFile.write(str(i))
    dataFile.write("\n")

