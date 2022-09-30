def bmi():
    check = input("Choose your height measure? - metre/cm\n: ")

    if check != "metre" and check != "cm":
        while True:
            check = input("Choose again? - >> metre or cm <<\n: ")
            if check == "metre":
                height = float(input("enter your height in m: "))
                break
            if check == "cm":
                height = float(input("enter your height in cm: "))
                height /= 100
                break

    elif check == "metre":
        height = float(input("enter your height in m: "))

    elif check == "cm":
        height = float(input("enter your height in cm: "))
        height /= 100

    weight = float(input("enter your weight in kg: "))
    bmi = round(weight / height ** 2, 2)

    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")
    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")
    elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinical obese")


bmi()





