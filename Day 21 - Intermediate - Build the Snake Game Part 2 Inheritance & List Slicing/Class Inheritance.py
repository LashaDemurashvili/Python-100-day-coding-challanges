# Class Inheritance

class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print("Inhale, Exhale")



class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Underwater")

    def swim(self):
        print("Moving in water")


lion = Animal()
lion.breath()

print("\n")

shark = Fish()
shark.breath()

