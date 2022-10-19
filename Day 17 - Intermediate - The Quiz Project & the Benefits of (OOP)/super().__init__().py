class Parent:

    def __init__(self, txt):
        self.message = txt

    def print_message(self):
        print(self.message)


class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)
        

y = Parent("Hello, Earth")
y.print_message()
Parent("Hello, Again").print_message()

print()

x = Child("Hello, World")
x.print_message()

