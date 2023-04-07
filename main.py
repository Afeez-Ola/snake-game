import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.register_shape("snake", ((-5, -5), (-5, 5), (0, 10), (5, 5), (5, -5), (0, -10)))

snake = Snake()
food = Food()

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

    if snake.segments[0].distance(food) < 15:
        food.refresh()

screen.exitonclick()
