from turtle import Turtle, Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


score = Scoreboard()

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong')
screen.tracer(0)  # for no animation, but than we need screen update

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = Turtle
while game_is_on:
    right_score = 0
    left_score = 0

    time.sleep(ball.ball_speed)  # for speed down a ball moving
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with both paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # R paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # L paddle missed
    if ball.xcor() < - 380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()




