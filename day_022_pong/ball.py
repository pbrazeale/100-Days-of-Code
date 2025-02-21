from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

    # def volley(self):
    #     self.setheading(random.randint(0, 360))
    #     self.forward(20)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.xcor() + 10
        self.goto(new_x, new_y)
