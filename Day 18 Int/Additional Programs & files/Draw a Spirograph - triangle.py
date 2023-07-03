# Draw a Spirograph

import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.speed(0)

def color_mode():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    color = (R, G, B)
    return color


def draw_spirograph(color, size_of_gap, circle_radius):
    angle = int(360 / size_of_gap)
    for _ in range(angle):
        tim.color(color)
        tim.circle(circle_radius)
        tim.left(size_of_gap)


x = 7
y = 70


# draw_spirograph(color_mode(), x, y)  # random color
draw_spirograph('red', x, y)

tim.setheading(0)
tim.forward(y*4)
# draw_spirograph(color_mode(), x, y)  # random color
draw_spirograph('green', x, y)

tim.setheading(120)
tim.forward(y*4)
# draw_spirograph(color_mode(), x, y)   # random color
draw_spirograph('blue', x, y)


screen = t.Screen()
screen.exitonclick()