"""
source link:
https://bobbyhadz.com/blog/python-iterate-over-object-attributes
"""

"""
1. Iterate over an Object's attributes in Python


Use the __dict__ attribute to get a dictionary containing the object's properties and values.
Use the dict.items() method to get a view of the dictionary's items.
Use a for loop to iterate over the object's attributes.

dict.items()
"""


class Employee:
    cls_id = 'employee'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee('lasha', 100)


for attribute, value in emp1.__dict__.items():
    print(attribute, value)
