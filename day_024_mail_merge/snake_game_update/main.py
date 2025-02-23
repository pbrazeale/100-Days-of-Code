from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

RIGHT_WALL = 290
LEFT_WALL = -290
TOP_WALL = 290
BOTTOM_WALL = -290

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.plop()
        snake.extend()
        scoreboard.score()

    # Detect collision with food.
    if (
        snake.head.xcor() > RIGHT_WALL
        or snake.head.xcor() < LEFT_WALL
        or snake.head.ycor() > TOP_WALL
        or snake.head.ycor() < BOTTOM_WALL
    ):
        game_is_one = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_one = False
            scoreboard.game_over()

screen.exitonclick()
