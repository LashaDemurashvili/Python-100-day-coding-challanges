# *args: Positional Variable-Length Arguments
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 2, 1, 7, 4, 3))


# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Cars:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.year = kw.get("year")
        self.color = kw.get("color")
        self.doors = kw.get("doors")
        self.speed = kw.get("speed")


mers = Cars(model='w140', color='black', doors=4, year=1990)
print(mers.model)
print(mers.color)
print(mers.doors)
print(mers.year)
print(mers.speed)
