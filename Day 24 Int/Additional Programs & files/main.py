"""
my_dict = {
    'name': 'lasha',
    'surname': 'demurashvili'
}
for i, [k, v] in enumerate(my_dict.items(), 1):
    print(f"{i}. {k} - {v}")


me = 'Hello my name is lasha demurashvili, and I am 25'
print(me.split())

print('my name'.ljust(10, '/'))

"""
import random

# code with nonajanashia
# recap


#
# def checking(test_data):
#     if (test_data.find('.') != -1):
#         return 'Float'
#     elif (test_data.isdigit()):
#         return "Number"
#     else:
#         return 'String'
#
#
# data = ['2.22', 100, 'apple', 'strawberry', 222, 33.3, ';']
#
# x = str(random.choice(data))
# print(f"{checking(x)} - '{x}'")

import colorama
from colorama import Fore

colorama.init()

x = 5
y = 0
try:
    print(x / y)
except Exception as ex:
    print(f"{Fore.RED}Error: {ex} {Fore.RESET}")
else:
    print(f"{Fore.GREEN}code execute successfully{Fore.RESET}")
finally:
    print("Program end!")

sentence = "This is a sample sentence"
r = sentence.replace(' ', '_')
print(r)

w = sentence.split()
print(w)

q = '_'.join(w)
print(q)

t = (4, 1, 2, 2, 3, 3, 4, 7)
s = {4, 1, 2, 2, 3, 3, 4, 7}
print(s)
print(type(s))


print(t)




print('*' * 100)

my_set = {'Jan', "Feb", "Mar", "Apr"}
for i in my_set:
    print(i)

print(list(my_set)[0:2])

dc = {"x": 'a'}
dc["x"] = input("value: ")

print(type(dc))
print(dc)