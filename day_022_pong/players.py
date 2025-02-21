from turtle import Turtle


class player(Turtle):
    def __init__(self):
        super().__init__()

    def paddle(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
