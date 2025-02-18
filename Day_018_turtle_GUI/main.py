import turtle as T

# from turtle import Turtle, Screen
import random

T.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_shape(name, num_sides, num_forward):
    angle = 360 / num_sides
    for _ in range(num_sides):
        name.forward(num_forward)
        name.right(angle)


def draw_random_walk(name, num_forward):
    angle = random.choice([0, 90, 180, 270])
    name.right(angle)
    name.forward(num_forward)


def draw_spirograph(name, circles, radius):
    angle = 360 / circles
    for _ in range(circles + 1):
        name.color(random_color())
        name.circle(radius)
        name.right(angle)


timmy = T.Turtle()
timmy.shape("turtle")
timmy.color("blue3")
timmy.pensize(3)
timmy.speed(0)

# such a clean solution!
# for _ in range(3, 11):
#     timmy.color(random.choice(colors))
#     draw_shape(timmy, _, 100)

# for _ in range(30):
#     timmy.color(random_color())
#     draw_random_walk(timmy, 20)

draw_spirograph(timmy, 60, 100)

screen = T.Screen()
screen.exitonclick()
