class Car:

    def __init__(self, brand, model, year, manufacture="Germany"):
        self.brand = brand
        self.model = model
        self.year = year
        self.manufacture = manufacture

    def printer(self):
        print(f"Year: {self.year}\n{self.brand}: {self.model}")
        print(f"Made in {self.manufacture}\n")


car_01 = Car("Mercedes-Benz", "W140", 1991, "GERMANY")
car_01.printer()


class eCar(Car):
    def __init__(self, brand, model, year, manufacture):
        super().__init__(brand, model, year, manufacture)


new_car = eCar("Smart", "Smartest", 2020, "China")
new_car.printer()


