# test function, automation

import string
from random import randint, choice

letters = string.ascii_letters
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_letters = [choice(letters) for _ in range(randint(8, 10))]
password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
password_numbers = [choice(numbers) for _ in range(randint(2, 4))]


def password_generator():
    # ln_of_pass = int(input('How many characters?: '))

    ln_of_pass = randint(10, 20)
    random_answers = ['yes', 'no']

    # ask_letters = input("letters? yes/no: ")
    # ask_numbers = input("numbers? yes/no: ")
    # ask_symbols = input("symbols? yes/no: ")

    ask_letters = choice(random_answers)
    ask_numbers = choice(random_answers)
    ask_symbols = choice(random_answers)

    password = ''
    while len(password) < ln_of_pass:
        if ask_letters == 'yes' and len(password) < ln_of_pass:
            password += choice(letters)
        if ask_numbers == 'yes' and len(password) < ln_of_pass:
            password += choice(numbers)
        if ask_symbols == 'yes' and len(password) < ln_of_pass:
            password += choice(symbols)

    print(len(password))
    print('length original:', ln_of_pass)
    print('ask_letters:', ask_letters)
    print('ask_numbers:', ask_numbers)
    print('ask_symbols:', ask_symbols)

    return password


password = password_generator()

print(password)
