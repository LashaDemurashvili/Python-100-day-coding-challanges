height = float(input("Enter height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height not to be over 3 meters!")
bmi = weight / height ** 2
print(bmi)
