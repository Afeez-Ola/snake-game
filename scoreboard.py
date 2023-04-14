from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


def read_high_score():
    with open("file.txt", mode="r") as file:
        content = file.read()
        return content


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.high_score = int(read_high_score())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(read_high_score()):
            self.high_score = self.score
            self.update_score()
        self.score = 0
        self.update_scoreboard()

    def scoring(self):
        self.score += 1
        self.update_scoreboard()

    def update_score(self):
        if self.high_score > int(read_high_score()):
            with open("file.txt", mode="w") as file:
                file.write(f"{self.high_score}")
            read_high_score()
