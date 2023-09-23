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
# day23 save_01

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

