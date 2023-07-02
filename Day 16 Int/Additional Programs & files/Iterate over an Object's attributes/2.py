"""
Iterate over an Object's attributes using vars()

An alternative to using the __dict__ attribute is to use the built-in vars() function.
"""

"""
The vars function takes an object and returns the __dict__ attribute of the given module, class, instance or any other
object that has a __dict__ attribute.
The vars() function raises a TypeError if the provided object doesn't have a __dict__ attribute.

"""

class Employee:
    cls_id = 'employee'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee('lasha', 100)

for attribute, value in vars(emp1).items():
    # name lasha
    # salary 100
    print(attribute, value)

