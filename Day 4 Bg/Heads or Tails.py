"""
Day 4 - Beginner - Randomisation and Python Lists

practice random module
"""
import random
import time


def mani_rand(prompt):
    def rand():
        random_side = random.randint(0, 1)
        if random_side == 1:
            return 1  # Head
        else:
            return 0  # Tail

    h = 0
    t = 0
    emp_ls = []

    for i in range(prompt):

        x = rand()
        if x == 1:
            emp_ls.append(x)
            h += 1
        else:
            emp_ls.append(x)
            t += 1

    print()
    print(f"{prompt:,} - Rolls Result")
    print()

    sm = h + t

    print(emp_ls[:10], "...", emp_ls[-10:])
    print(f"{h} - Head - {round(h / sm * 100, 2)}%")
    print(f"{t} - Tails - {round(t / sm * 100, 2)}%")

    print("*" * 70)


test_list = [10, 50, 100, 1000, 10000, 100000]

# calculate how many seconds needs program
start = time.time()

for i in test_list:
    mani_rand(i)

end = time.time()
print(f"{end-start} - seconds")