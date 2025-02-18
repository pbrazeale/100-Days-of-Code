import turtle as T
import colorgram
import random

T.colormode(255)

colors = colorgram.extract("image.jpg", 10)

timmy = T.Turtle()
timmy.pensize(10)
timmy.speed(0)


def color_paint_brush(i):
    paint_color = colors[i]
    return paint_color.rgb


def bottom_right(name, height, width):
    name.up()
    name.right(90)
    name.forward((height / 2))
    name.right(90)
    name.forward((width / 2))
    name.right(180)
    name.down()


def draw_dots_row(name, dots, grid_width):
    for _ in range(dots):
        name.color(color_paint_brush(random.randint(0, 9)))
        name.forward(1)
        if _ < dots - 1:
            name.up()
            name.forward(grid_width)
            name.down()


def painting(name, height, width, dots):
    grid_width = width / dots - dots
    grid_height = height / dots - dots
    bottom_right(name, height, width)
    for _ in range(dots):
        draw_dots_row(name, dots, grid_width)
        if _ < dots - 1:
            name.up()
            name.left(90)
            name.forward(grid_height)
            name.left(90)
            name.forward(grid_width * 9 + 10)
            name.right(180)
            name.down()


painting(timmy, 800, 800, 10)


# print(color_paint_brush(random.randint(0, 9)))

screen = T.Screen()
screen.exitonclick()
