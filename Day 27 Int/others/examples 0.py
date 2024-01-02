# *args
def add(*args):
    sm = sum(args)
    print(sm)


add(1, 2, 3, 4, 5)

print("-" * 50)


def calculator(n, **kwargs):
    print(kwargs)  # returned as dict
    n += kwargs["add"]
    n -= kwargs["subtract"]
    print(n)


calculator(3, add=5, subtract=2)
#  3 + 5 - 2
print("-" * 50)


class Car:
    def __init__(self, **kw):
        self.brand = kw.get("brand")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.cost = kw.get("cost")

        # print(kw)  # created dict - key: value


car_1 = Car(brand="Bmw", model="X6", color="Black", cost="20 000")
print(car_1.brand)





print("-" * 50)

# calculator - we can choose each operation, or stay as it default
def calculator(n, add=0, subt=0, mult=1, divide=1):
    n += add
    n -= subt
    n *= mult
    n /= divide
    print(n)


calculator(10, add=15, divide=3, mult=4)
calculator(10, add=12)  # add
calculator(10, subt=4)  # subtract
calculator(7, mult=7)  # multiply
calculator(6, divide=2)  # divide