"""
If you need to include the class variables when iterating, use the dir() function.

# Iterate over an Object's attributes using dir()
"""

"""
1. Use the dir() function to get a list of the names of the object's attributes.
2. Optionally filter out attributes that start with two underscores and methods.
3. Use a for loop to iterate over the object's attributes.
"""


class Employee:
    cls_id = 'employee'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee('lasha', 100)

attributes = [attribute for attribute in dir(emp1)
              if not attribute.startswith('__')]
print(attributes)  # 👉️ ['cls_id', 'name', 'salary']

for attr in attributes:
    # cls_id employee
    # name lasha
    # salary 100
    print(attr, getattr(emp1, attr))
