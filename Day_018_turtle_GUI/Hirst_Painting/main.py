import turtle as T
import colorgram
import random

colors = colorgram.extract("image.jpg", 10)

timmy = T.Turtle()

timmy.pensize(30)


def painting(name, height, width, dots):
    grid_width = width / dots - dots
    grid_height = height / dots - dots
    for _ in range(dots + 1):
        name.color(random.choice(colors))
        name.forward(1)
        name.up
        name.forward(grid_width)
        name.down()


painting(timmy, 200, 200, 10)
