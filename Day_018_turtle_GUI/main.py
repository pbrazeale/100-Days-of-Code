from turtle import Turtle, Screen


def draw_square(num):
    # i = 4
    # while i > 0:
    #     timmy.forward(num)
    #     timmy.right(90)
    #     i -= 1
    for _ in range(4):
        timmy.forward(num)
        timmy.right(90)


timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue3")
draw_square(100)

screen = Screen()
screen.exitonclick()
