
# option 1

def checkleap(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Year is a >> leap <<")
    else:
        print("Year > isn't a leap <")


year = int(input("Enter the year: "))

checkleap(year)

# option 2

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
