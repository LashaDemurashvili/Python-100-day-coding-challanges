from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=700, height=500)

user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win? Enter color: ")

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'purple', 'magenta']

all_turtles = []

pos_x = -330    # edge of canvas
pos_y = -150
for pos in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[pos])   # color[0] = 'red'
    new_turtle.goto(x=pos_x, y=pos_y)
    all_turtles.append(new_turtle)

    pos_y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 320:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(1, 11)
        turtle.forward(random_distance)



screen.exitonclick()