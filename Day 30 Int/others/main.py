# add random numbers range to data.txt
from random import randint


def append_txt():
    with open("data.txt", "a") as dataFile:
        random_number = randint(1, 30)
        for i in range(random_number):
            file = dataFile.write(str(i))
        dataFile.write("\n")


# append_txt()


def read_txt():
    with open("data.txt") as dataFile:
        data = dataFile.readlines()
        r = [i.replace("\n", "") for i in data]
        return r


print(read_txt())
