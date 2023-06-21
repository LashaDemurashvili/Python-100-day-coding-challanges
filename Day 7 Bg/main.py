"""
Program Descriptions

Day 7 - Beginner - Hangman

"""

import random
from recources.hangman_words import word_list
from recources.hangman_art import stages, logo

print(logo)

end_of_game = False
lives = 6

passed_wrong = ""

chosen_word = random.choice(word_list)

display = ["_" for x in chosen_word]

# Hint
hint = input("Dou you want a hint?: yes/no \n: ").lower()
if hint == "yes":
    print(
        f'Hint - Word is starting >> {chosen_word[0]} ... and ending ... {chosen_word[-1:]} << \nlength is {len(chosen_word)}')
    display = ["_" for x in chosen_word]
    display[0] = chosen_word[0];
    display[-1:] = chosen_word[-1:]
    print(f"{display}")
elif hint == "no":
    print("Ok good luck")
else:
    print("You lost your chance :( don't worry go ahead")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display and display.count(guess) == chosen_word.count(guess):
        print(f"You've already guess {guess}")

    elif guess in passed_wrong:
        print(f"You've already choose {guess} which is not correct!")

    elif guess in chosen_word:
        if display.count(guess) < chosen_word.count(guess):
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = guess
            print(f"Correct letter")
    else:
        passed_wrong += guess
        lives -= 1
        print(f"You lost 1 life\n{lives} try is remaining")

    if lives == 0:
        end_of_game = True
        print("You Lose!")
        print(f"Correct word was >> {chosen_word} <<")

    elif "_" not in display and lives > 0:
        end_of_game = True
        print(f"Yes it's a >> {chosen_word} <<")
        print("You Win!")

    print(display)
    print(stages[lives])
