from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('green')


def square():
    for _ in range(4):
        tim.forward(100)
        tim.left(90)


square()

tim.forward(50)
tim.circle(50)
tim.circle(40)
tim.circle(30)
tim.circle(20)
tim.circle(10)


screen = Screen()
screen.exitonclick()

