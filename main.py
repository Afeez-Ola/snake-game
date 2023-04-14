import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.register_shape("snake", ((-5, -5), (-5, 5), (0, 10), (5, 5), (5, -5), (0, -10)))

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    scoreboard.update_scoreboard()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.scoring()
        snake.extend_segment()

    if snake.segments[0].xcor() > 285 or snake.segments[0].xcor() < -285 or snake.segments[0].ycor() > 285 or \
            snake.segments[0].ycor() < -285:
        time.sleep(0.2)
        scoreboard.reset()
        snake.reset()
    elif snake.segments[-1].xcor() > 290 or snake.segments[-1].xcor() < -290 or snake.segments[-1].ycor() > 285 or \
            snake.segments[-1].ycor() < -285:
        time.sleep(0.2)
        scoreboard.reset()
        snake.reset()
    pos = 0

    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            time.sleep(0.2)
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
