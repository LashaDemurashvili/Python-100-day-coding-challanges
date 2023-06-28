"""
Day 14 - Beginner - Higher Lower Game Project
"""
from recources.art import logo, vs
from recources.game_data import data
import colorama as cl
from colorama import Fore, Back
import random

cl.init(autoreset=True)


# Get random data; which is list and in list is dict [{key:vale}, {key:vale}, {key:vale}]
def random_account():
    return random.choice(data)


# define printed data format
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    # testing
    # print(f'{Fore.LIGHTRED_EX} {name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


# compare which is greater
# and return True or False
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"  # check if guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True

    account_a = random_account()
    account_b = random_account()

    # change only when b is correct b became a
    # when 'a' is correct a became new random variable from data/ not stay as it
    while game_should_continue:
        account_a = account_b
        account_b = random_account()

        # avoid thad don't have same data
        while account_a == account_b:
            account_b = random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        # returned True or False

        print(logo)

        # if True:
        if is_correct:
            score += 1
            print(f"{Fore.GREEN}You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"{Fore.RED}Sorry, that's wrong. Final score: {score}")

    if input("You want a new game ? y/n: ") == "y":
        print(f"{Fore.LIGHTBLUE_EX}New Game Start")
        game()
    else:
        print("Good bay!")


text = " Guess which has more followers on instagram "
print(f"{Fore.YELLOW} {text.center(len(text) * 2, '*').title()}")

game()


'''
FAQ: Why does choice B always become choice A in every round, even when A had more followers? 
Suppose you just started the game and you are comparing the followers of A - Instagram (364k) 
to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison
should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer 
followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would 
stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a 
situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)

# Generate a random account from the game data.
# Format account data into printable format.
# Ask user for a guess.
# Check if user is correct.
## Get follower count.
## If Statement
# Feedback.
# Score Keeping.
# Make game repeatable.
# Make B become the next A.
# Add art.
# Clear screen between rounds.
'''