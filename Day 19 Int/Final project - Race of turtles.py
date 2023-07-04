from turtle import Turtle, Screen
import random
import colorama as cl
from colorama import Fore, Back

cl.init(autoreset=True)

is_race_on = False
screen = Screen()
screen.setup(width=700, height=500)

user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win? Enter color: ")

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'magenta']

all_turtles = []

pos_x = -330  # edge of canvas
pos_y = -150
for pos in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[pos])  # color[0] = 'red'
    new_turtle.goto(x=pos_x, y=pos_y)
    all_turtles.append(new_turtle)

    pos_y += 50


# just to colorizing winner text
def checking_winner_color(color):
    if color == "red":
        return Fore.RED
    elif color == "green":
        return Fore.GREEN
    elif color == "blue":
        return Fore.BLUE
    elif color == "orange":
        return Fore.LIGHTYELLOW_EX
    elif color == "yellow":
        return Fore.YELLOW
    elif color == "purple":
        return Fore.LIGHTMAGENTA_EX
    elif color == "magenta":
        return Fore.MAGENTA


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 310:  # so if turtle reach end of the canvas
            is_race_on = False
            winning_color = turtle.pencolor()  # get current pen color which is use

            w_color = checking_winner_color(winning_color)
            if winning_color == user_bet:
                print(f"{w_color}You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"{Back.RED}You've lost! {Back.RESET}The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        random_distance = random.randint(1, 11)
        turtle.forward(random_distance)

        ## advance plan - just all forward at same speed
        # turtle.forward(7)

screen.exitonclick()
