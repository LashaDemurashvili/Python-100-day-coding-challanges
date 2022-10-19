from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(-60, 0)
        self.write("Game over", align='left', font=FONT)
