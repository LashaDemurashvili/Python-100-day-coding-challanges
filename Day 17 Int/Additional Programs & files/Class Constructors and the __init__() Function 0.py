# Working with Attributes, Class Constructors and the __init__() Function

class User:

    def __init__(self, user_id, username, follower=0):  # default value: = default
        self.id = user_id
        self.username = username
        self.follower = follower

    def printer(self):
        print(f"User ID: {self.id} \nUser: {self.username} \nFollowers: {self.follower}")


# if we don't assign any parameter of > follower <  this will be >> default - 0 <<


user_01 = User(1, "Jeka")
user_01.printer()

print()
# now follower will be 77
user_02 = User(2, "lasha", 77)
user_02.printer()

print()


# same method we can do that
class Person:

    def __init__(self, f_name, l_name):  # default value: = default
        self.first_name = f_name
        self.last_name = l_name
        self.region = "GEORGIA"

    def printer(self):
        print(f"{self.first_name} \n{self.last_name} \n{self.region}")


# region always will be GEORGIA, we can't change that except of first method


individual_01 = Person("lasha", "Demurashvili")
individual_01.printer()
