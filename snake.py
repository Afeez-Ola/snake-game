import time
from turtle import Screen, Turtle

move_distance = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.starting_positions = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]

        for position in self.starting_positions:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)
        self.segments[0].left(90)

# Snake()
# screen = Screen()
# screen.exitonclick()
