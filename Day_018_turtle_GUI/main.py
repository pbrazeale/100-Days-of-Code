from turtle import Turtle, Screen


def draw_triangle(name, num):
    for _ in range(3):
        name.forward(num)
        name.right(120)


def draw_square(name, num):
    for _ in range(4):
        name.forward(num)
        name.right(90)


def draw_pentagon(name, num):
    for _ in range(5):
        name.forward(num)
        name.right((72))


def draw_hexagon(name, num):
    for _ in range(6):
        name.forward(num)
        name.right((60))


def draw_heptagon(name, num):
    for _ in range(7):
        name.forward(num)
        name.right((51.4285))


def draw_octagon(name, num):
    for _ in range(8):
        name.forward(num)
        name.right((45))


def draw_nonagon(name, num):
    for _ in range(9):
        name.forward(num)
        name.right((40))


def draw_decagon(name, num):
    for _ in range(10):
        name.forward(num)
        name.right((36))


def draw_dash_line(name, num):
    line = round(num / 20)
    for _ in range(int(num / (line * 2))):
        name.forward(line)
        name.penup()
        name.forward(line)
        name.pendown()


def draw_shape(name, num_sides, num_forward):
    angle = 360 / num_sides
    for _ in range(num_sides):
        name.forward(num_forward)
        name.right(angle)


timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue3")
# draw_square(name, 100)
# draw_dash_line(timmy, 100)

# draw_triangle(timmy, 100)
# draw_square(timmy, 100)
# draw_pentagon(timmy, 100)
# draw_hexagon(timmy, 100)
# draw_heptagon(timmy, 100)
# draw_octagon(timmy, 100)
# draw_nonagon(timmy, 100)
# draw_decagon(timmy, 100)

# such a clean solution!
for _ in range(3, 11):
    draw_shape(timmy, _, 100)

screen = Screen()
screen.exitonclick()
