from turtle import Turtle
from food import Food

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.high_score = 0
        # self.scoring()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0


    def scoring(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

# print(Scoreboard().score)
