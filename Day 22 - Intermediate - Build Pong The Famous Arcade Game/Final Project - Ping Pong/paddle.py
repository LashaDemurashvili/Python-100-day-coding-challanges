from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        self.position = position
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)  # 5 * 20 , 1 * 20
        self.color('white')
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)


    def go_down(self):
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)

