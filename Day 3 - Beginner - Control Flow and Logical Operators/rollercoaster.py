print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")

    age = int(input("Enter your age: "))
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age < 18:
        print("Youth tickets are $7.")
        bill = 7
    elif 45 <= age <= 55: # same as: age >= 45 and age <= 55
        print("Free ticket !")
        bill = 0
    else:
        print("Adult tickets are $12.")
        bill = 12

    print("Photo price is $3")
    wants_photo = input("Dou you want photo? Y / N: ")
    if wants_photo == "Y":
        bill += 3
    print(f"The total bill is ${bill}")
else:
    print("You can't ride")
