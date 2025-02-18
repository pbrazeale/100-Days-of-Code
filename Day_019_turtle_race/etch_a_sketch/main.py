import turtle as T

screen = T.Screen()
timmy = T.Turtle()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def clockwise():
    timmy.right(36)


def counter_clockwise():
    timmy.left(36)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


def main():
    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="d", fun=clockwise)
    screen.onkey(key="a", fun=counter_clockwise)
    screen.onkey(key="c", fun=clear_screen)

    screen.exitonclick()


main()
