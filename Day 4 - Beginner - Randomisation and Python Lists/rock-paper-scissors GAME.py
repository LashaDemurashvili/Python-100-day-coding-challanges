# rock-paper-scissors GAME

import random
import string
str = string.ascii_lowercase


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
wins = 0
lose = 0
draw = 0

print("For exit game please type: >> q <<")
while True:
    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n: ")
    if len(user_choice) > 1:
        print("To many characters, we need >> one <<")
        break

    elif len(user_choice) == 1:
        if user_choice in str:
            if user_choice != "q":
                print("You type string, but we need integer for proceed")
                break
            print("GAME END")
            break

    user_choice = int(user_choice)

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
        break
    elif user_choice == 0:
        print(f"User chose: \n\tRock \n{game_images[user_choice]}")
    elif user_choice == 1:
        print(f"User chose: \n\tPaper \n{game_images[user_choice]}")
    else:
        print(f"User chose: \n\tScissors \n{game_images[user_choice]}")

    computer_choice = random.randint(0, 2)
    x = computer_choice

    if x == 0:
        print(f"Computer chose: \n\tRock \n{game_images[x]}")
    elif x == 1:
        print(f"Computer chose: \n\tPaper \n{game_images[x]}")
    else:
        print(f"Computer chose: \n\tScissors \n{game_images[x]}")

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
        wins += 1
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
        lose += 1
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
        wins += 1
    elif computer_choice == user_choice:
        draw += 1
        print("It's a draw")

print(f"Your wins is : {wins}\nYour lose is {lose}\nYour draw is {draw}")
