import random as r
import turtle as t

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = t.Turtle()

# option 1
def draw_shapes():
    sides = 3
    for x in range(3, 11):
        tim.color(r.choice(colours))
        for _ in range(sides):
            tim.right(360 / sides)
            tim.forward(100)
        sides += 1

# draw_shapes()


# option 2
def draw_shapes_option_2():
    def draw_shape(num_side):
        angle = 360 / num_side
        for _ in range(num_side):
            tim.right(angle)
            tim.forward(100)


    for shape_side_n in range(3, 11):
        tim.color(r.choice(colours))
        draw_shape(shape_side_n)


draw_shapes_option_2()



screen = t.Screen()
screen.exitonclick()
