print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n: ")
name2 = input("What is their name?\n: ")

combine_strings = name1 + name2
lower_case_string = combine_strings.lower()
l_c_s = lower_case_string

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

love_score = int(str(true) + str(love))

print(f"Your love score is {love_score}")

if (love_score < 10) or (love_score > 90):
    print(f"Your score is **{love_score}**, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is **{love_score}**, you are alright together.")
else:
    print(f"Your score is **{love_score}**.")

