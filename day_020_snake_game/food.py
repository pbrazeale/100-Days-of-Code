from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.plop()

    def plop(self):
        random_x = random.randint(-28, 28) * 10
        random_y = random.randint(-28, 28) * 10
        self.goto(random_x, random_y)
