"""
Program Descriptions
Day 5 - Beginner - Python Loops

Program Descriptions:
odd even numbers
"""

total_even = 0
total = 5050

for i in range(2, 101, 2):
    total_even += i
    total -= i

print(total_even, "even")
print(total, "odd")

print("\n")
print("option 2\n")

even = 0
odd = 0
for i in range(101):
    if i % 2 == 0:
        even += i
    else:
        odd += i

print(even, "even")
print(odd, "odd")

print((even + odd) == 5050)


