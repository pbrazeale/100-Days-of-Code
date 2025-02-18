from turtle import Turtle, Screen


def draw_square(name, num):
    # i = 4
    # while i > 0:
    #     timmy.forward(num)
    #     timmy.right(90)
    #     i -= 1
    for _ in range(4):
        name.forward(num)
        name.right(90)


def draw_dash_line(name, num):
    line = round(num / 20)
    for _ in range(int(num / (line * 2))):
        name.forward(line)
        name.penup()
        name.forward(line)
        name.pendown()


timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue3")
# draw_square(name, 100)
draw_dash_line(timmy, 100)

screen = Screen()
screen.exitonclick()
