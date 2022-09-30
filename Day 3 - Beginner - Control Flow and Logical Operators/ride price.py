height = float(input("Enter your height: "))

if height > 120:
    age = int(input("Enter your age: "))
    if age < 12:
        print("you can ride\nPrice is $5")
    elif age <= 18:
        print("you can ride\nPrice is $7")
    else:
        print("you can ride\nPrice is $12")
else:
    print("You can't ride")
