from turtle import Turtle

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
        self.read_high_score()
        # self.scoring()

    def update_scoreboard(self):
        self.write_high_score()
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        self.read_high_score()

    def write_high_score(self):
        with open("file.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def read_high_score(self):
        with open("file.txt", mode="r") as file:
            file.read()

    def scoring(self):
        self.score += 1
        self.update_scoreboard()


# print(Scoreboard().score)
