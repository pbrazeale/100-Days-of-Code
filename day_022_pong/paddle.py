from turtle import Turtle


class Paddle(Turtle):
    # Creates the paddle object
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # Give go_up method
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Give go_down method
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
