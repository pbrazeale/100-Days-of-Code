from turtle import Turtle


class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_loop(self, state, position):
        self.goto(position)
        self.write(state)
