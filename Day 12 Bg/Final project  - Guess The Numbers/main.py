"""
Final project  - Guess The Numbers

generate random number from 1 to 100
ask user number
check if user guess the number
"""

from recources.art import logo
import random
import colorama
from colorama import Fore, Back, Style

# Initialize colorama
colorama.init(autoreset=True)


def guess_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # generate random number
    rand_number = random.randint(1, 100)

    # test
    print(rand_number)

    try:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            attempts = 10
        else:
            attempts = 5
        print(f"You have {attempts} attempts remaining to guess the number")

        while True:
            if attempts == 0:
                print(f"{Fore.LIGHTRED_EX}You lose !!!")
                break

            print(f"You have >> {attempts} << attempts")
            guess_num = int(input("Make a guess: "))

            if guess_num == rand_number:
                print(f"{Fore.LIGHTGREEN_EX} You Win !!!")
                break
            elif guess_num > rand_number:
                print("Guess again.")
                print(f"X <<< {guess_num} is too high")
                attempts -= 1
            elif guess_num < rand_number:
                print("Guess again.")
                print(f"{guess_num} is too low >>> X")
                attempts -= 1
    except Exception as e:
        print(f"{Back.BLACK} {Fore.RED} {e}")
        print(f"{Fore.GREEN} Program RESTARTED")

        guess_number()
    else:
        if input("You want to play again? y/n \n: ") == "y":
            print(f"{Fore.LIGHTCYAN_EX}New Game START")
            guess_number()
        else:
            print(f"{Fore.LIGHTBLUE_EX}Program END !")


guess_number()
