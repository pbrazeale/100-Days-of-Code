from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()

game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
