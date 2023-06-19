"""
Day 3 - Beginner - Control Flow and Logical Operators

Program Descriptions:
checking if year is leap or not

Condition of the task:
see the dir ==> Conditions - Flow Charts/Leap_Year_1.png
see the dir ==> Conditions - Flow Charts/Leap_Year_2.png

"""


# option 1

def checkleap(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("\t" * 5, "Year is a >> leap <<", year)
    else:
        print("Year > isn't a leap <")


# year = int(input("Enter the year: "))


# testing program
test_list = list(range(2000, 2023, 1))
# print(test_list)

for y in test_list:
    checkleap(y)

print("*" * 50)


# option 2
def lp(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.", year)
            else:
                print("Not leap year.")
        else:
            print("Leap year.", year)
    else:
        print("Not leap year.")


# lp()

for i in test_list:
    lp(i)
