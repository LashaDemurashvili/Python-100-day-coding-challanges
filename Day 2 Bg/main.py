"""
Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings

Program Descriptions:
Project -  Tip Calculator

Condition of the task:
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.

"""
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $\n: "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? in %\n: "))
person = int(input("How many people to split the bill?\n: "))

tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / person

# first approach
final_result = round(bill_per_person, 2)
print(f"Each person should pay: ${final_result}")

# second approach
result = round((bill + (bill*tip/100)) / person, 2)
print(f"Each person should pay: ${result}")

# third approach
final_result_1 = "{:.2f}".format(bill_per_person)
# for this result - $33.60
print(f"Each person should pay: ${final_result_1}")
