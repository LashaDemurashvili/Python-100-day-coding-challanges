"""
Day 3 - Beginner - Control Flow and Logical Operators

Program Descriptions:

Condition of the task:
check how many times repeat characters to both name
"""

print("Welcome to the Love Calculator!")
while True:
    name1 = input("What is your name?\n: ")
    if not name1.isdigit():
        break

while True:
    name2 = input("What is their name?\n: ")
    if not name1.isdigit():
        break

def delimeter():
    print("\n", "*" * 30)


combine_strings = name1 + name2
lower_case_string = combine_strings.lower()
l_c_s = lower_case_string

# easy option
"""
t = l_c_s.count("t")
r = l_c_s.count("r")
u = l_c_s.count("u")
e = l_c_s.count("e")

true = t+r+u+e

print(f"T occurs {t} times")
print(f"R occurs {r} times")
print(f"U occurs {u} times")
print(f"E occurs {e} times")

print(f"Total = {true}")
"""

# best way
true_ls = ["t", "r", "u", "e"]

sm_true = 0
for char in true_ls:
    x = l_c_s.count(char)
    print(f"{char.upper()} occurs {x} times")
    sm_true += x

print(f"Total 'true' score = {sm_true}")
delimeter()

# easy way
"""
l = l_c_s.count("l")
o = l_c_s.count("o")
v = l_c_s.count("v")
e = l_c_s.count("e")

love = l+o+v+e

print(f"L occurs {l} times")
print(f"O occurs {o} times")
print(f"V occurs {v} times")
print(f"E occurs {e} times")

print(f"Total = {love}")
"""

# best way
love_ls = ["l", "o", "v", "e"]

sm_love = 0
for ch in love_ls:
    y = l_c_s.count(ch)
    print(f"{ch.upper()} occurs {y} times")
    sm_love += y

print(f"Total 'love' score = {sm_love}")
delimeter()

love_score = int(str(sm_true) + str(sm_love))

print(f"Your love score is {love_score}")
delimeter()

if (love_score < 10) or (love_score > 90):
    print(f"Your score is **{love_score}**, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is **{love_score}**, you are alright together.")
else:
    print(f"Your score is **{love_score}**.")
