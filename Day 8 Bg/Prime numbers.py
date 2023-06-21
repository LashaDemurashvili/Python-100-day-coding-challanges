"""
Instructions
Prime numbers are numbers that can only be cleanly divided by themselves and 1.
You need to write a function that checks
whether if the number passed into it is a prime number or not.e.g. 2 is a prime number because it's only divisible
by 1 and 2.But 4 is not a prime number because you can divide it by 1, 2 or 4.
"""

pr = []
nt_pr = []


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    return is_prime


print("not prime","|" ,"prime")
for i in range(1, 100):
    if prime_checker(i):
        pr.append(i)
        print("\t" * 3, i)
    else:
        nt_pr.append(i)
        print(i)

print('\n')
print(pr)
print(nt_pr)
