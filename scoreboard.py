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
        # self.scoring()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0.0, 0.0)
        self.write("Game Over!", move=False, align=ALIGNMENT, font=FONT)

    def scoring(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

# print(Scoreboard().score)
