
"""
The example uses the __dict__ attribute to get a dictionary containing the object's properties and values.
"""

class Employee:
    cls_id = 'employee'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee('lasha', 100)

# 👇️ {'name': 'lasha', 'salary': 100}
print(emp1.__dict__)
