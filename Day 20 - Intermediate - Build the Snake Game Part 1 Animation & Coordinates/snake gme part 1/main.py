from turtle import Screen
import time
from snake import Snake


screen = Screen()
screen.setup(width=777, height=700)
screen.bgcolor('black')
screen.title("Welcome to Nokia 3310 Snake Game")
screen.tracer(0)


# create object snake
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()