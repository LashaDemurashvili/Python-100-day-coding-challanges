from recources.art import logo
import random


def guess_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    rand_number = random.randint(1, 100)

    # test
    # print(rand_number)

    ask_0 = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if ask_0 == "hard":
        attempts = 5
    else:
        attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number")

    while True:
        if attempts == 0:
            print("You lose")
            break

        print(f"You have >> {attempts} << attempts")
        guess_num = int(input("Make a guess: "))

        if guess_num == rand_number:
            print("You Win")
            break
        elif guess_num > rand_number:
            print("Guess again.")
            print(f"X <<< {guess_num} is too high")
            attempts -= 1
        elif guess_num < rand_number:
            print("Guess again.")
            print(f"{guess_num} is too low >>> X")
            attempts -= 1


guess_number()
