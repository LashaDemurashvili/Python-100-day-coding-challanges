"""
Day 10 - Beginner - Functions with Outputs

"""


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You should write both > first and last < name"
    return f"{f_name} {l_name}".title()


# print(format_name(input("What is your first name?: "), input("What is your last name?: ")))

f_1 = input("What is your first name?: ")
l_1 = input("What is your last name?: ")

print(format_name(f_1, l_1))
