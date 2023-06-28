"""
Day 12 - Beginner - Scope & Number Guessing Game
Final project  - Guess The Numbers

generate random number from 1 to 100
ask user number
check if user guess the number
"""

from recources.art import logo
import random
import colorama as cl
from colorama import Fore, Back, Style

# Initialize colorama
cl.init(autoreset=True)

# create lists to calculate final result
results_list = []

# create dict to calculate final result
results_dict = {
    "win": 0,
    "loss": 0,
}


def guess_number():
    # generate random number
    f_num = 1
    l_num = 20
    rand_number = random.randint(f_num, l_num)

    # welcome
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {f_num} and {l_num}.")

    # test
    print(rand_number)

    try:
        level = input("Choose a difficulty. Type 'e'/'easy' or 'h'/'hard': ")
        if level == "hard" or level == "h":
            attempts = 5
        else:
            attempts = 10
        print(f"You have {attempts} attempts remaining to guess the number")

        while True:
            if attempts == 0:
                print(f"{Fore.LIGHTRED_EX}You lose !!!")

                # append to list: 1 is win 0 is loss
                results_list.append(0)

                # update dict value
                results_dict["loss"] += 1
                break

            print(f"You have >> {attempts} << attempts")
            guess_num = int(input("Make a guess: "))

            if guess_num == rand_number:
                print(f"{Fore.LIGHTGREEN_EX} You Win !!!")

                # append to list 1 is win 0 is loss
                results_list.append(1)

                # update dict value
                results_dict["win"] += 1
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

        # if error occur call again program
        guess_number()
    else:
        # if code execute without any error
        if input("You want to play again? y/n \n: ") == "y":
            print(f"{Fore.LIGHTCYAN_EX}New Game START")

            # call again program and start new game
            guess_number()
        else:
            print(f"{Fore.LIGHTBLUE_EX}Program END !")

            # approach 1 using list to calculate final result
            """
            w = results.count(1)
            l = results.count(0)

            r = round(w / (w + l) * 100, 2)
            print(f"Win ration is: {r}%")
            """

            # approach 2 using dict to calculate final result
            win = results_dict["win"]
            loss = results_dict["loss"]

            res = round(win / (win + loss) * 100, 2)
            print(f"{Fore.YELLOW}Win ratio is: {res}% ")


guess_number()

# comment here
