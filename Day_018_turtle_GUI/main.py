from turtle import Turtle, Screen
import random

colors = ["blue3", "red", "black", "green", "purple"]


def draw_shape(name, num_sides, num_forward):
    angle = 360 / num_sides
    for _ in range(num_sides):
        name.forward(num_forward)
        name.right(angle)


def draw_random_walk(name, num_forward):
    angle = random.choice([0, 90, 180, 270])
    name.right(angle)
    name.forward(num_forward)


timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue3")
timmy.pensize(10)
timmy.speed(0)

# such a clean solution!
# for _ in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(timmy, _, 100)

for _ in range(30):
    timmy.color(random.choice(colors))
    draw_random_walk(timmy, 20)

screen = Screen()
screen.exitonclick()
