from recources.art import logo, vs
from recources.game_data import data

import random

def printer(account):
    name = account['name']
    description = account['description']
    country = account['country']
    print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


# generate random values
def random_value():
    return random.choice(data)

# compare which is greater
def compare(a, b):
    if a > b:
        return "a"
    else:
        return "b"


def game():
    print(logo)
    score = 0
    x = random_value()
    y = random_value()

    while True:
        # # if account a: a stay a, and b became new random value
        # if x['follower_count'] > y['follower_count']:
        #     x = x
        #     y = random_value()
        # else:
        #     x = y
        #     y = random_value()

        # every time even then correct is a: a will change with b and, b became new random value
        x = y
        y = random_value()

        # if x == y: we need they both to be different, so we need new random value
        while x == y:
            y = random_value()

        print(f"Compare_A: {printer(x)}")

        print(vs)

        print(f"Compare_B: {printer(y)}")

        ask_0 = input("Who has more followers? Type 'A' or 'B': ").lower()

        if compare(x['follower_count'], y['follower_count']) == ask_0:
            score += 1
            if y['follower_count'] > x['follower_count']:
                x = y
            else:
                x = x
            print(f"You're right! Current score: >> {score} <<.")
        else:
            print(f"Sorry, that's wrong. Final score: >> {score} <<")
            break
    print(f"Game is over")

print("*"*10, "Guess which has more followers on instagram".title(), "*"*10)
game()



