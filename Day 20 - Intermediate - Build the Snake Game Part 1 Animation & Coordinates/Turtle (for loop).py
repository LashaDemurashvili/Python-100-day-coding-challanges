from turtle import Turtle, Screen

tim = Turtle()
tim.speed(100)


for i in range(120):
    tim.color('cyan')
    tim.circle(i)
    tim.left(5)


screen = Screen()
screen.exitonclick()


