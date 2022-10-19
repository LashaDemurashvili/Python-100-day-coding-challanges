# Generate a Random Walk

import random
import turtle as t

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = t.Turtle()
tim.pensize(10)


tim.speed(0)

# same
# tim.speed('fastest')
"""
“fastest”: 0
“fast”: 10
“normal”: 6
“slow”: 3
“slowest”: 1"""


direction = [0, 90, 180, 270]


for _ in range(100):
    tim.color(random.choice(colours))
    tim.forward(20)
    tim.setheading(random.choice(direction))




screen = t.Screen()
screen.exitonclick()
