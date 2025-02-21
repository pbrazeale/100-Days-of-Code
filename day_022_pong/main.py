from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Remake")
screen.setup(800, 600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

# test
screen.exitonclick()
