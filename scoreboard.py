from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        # self.scoring()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 18, "normal"))

    def scoring(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

# print(Scoreboard().score)
