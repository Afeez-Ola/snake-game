from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]

for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(position)




















screen.exitonclick()
