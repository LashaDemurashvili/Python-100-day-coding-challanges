"""
Day 3 - Beginner - Control Flow and Logical Operators

Program Descriptions:

Condition of the task:
see the dir ==> Conditions - Flow Charts/BMI-Range.png
"""


def bmi_func():
    check = input("Choose your height measure? - m(metre)/c(cm)\n: ")

    if check != "m" and check != "c":
        while True:
            check = input("Choose again? - >> m or c <<\n: ")
            if check == "m":
                height = float(input("enter your height in m: "))
                break
            if check == "c":
                height = float(input("enter your height in cm: "))
                height /= 100
                break

    elif check == "m":
        height = float(input("enter your height in meter: "))

    elif check == "c":
        height = float(input("enter your height in cm: "))
        height /= 100

    weight = float(input("enter your weight in kg: "))
    bmi = round(weight / height ** 2, 2)

    temp = f"Your BMI is {bmi}"

    if bmi < 18.5:
        print(f"{temp}, you are underweight.")
    elif bmi < 25:
        print(f"{temp}, you have a normal weight.")
    elif bmi < 30:
        print(f"{temp}, you are slightly overweight.")
    elif bmi < 35:
        print(f"{temp}, you are obese.")
    else:
        print(f"{temp}, you are clinical obese")


# calling the function
bmi_func()
