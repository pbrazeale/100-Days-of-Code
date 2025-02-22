from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_X = 295


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        all_cars = []

    def create_cars(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.left(180)
        self.shapesize(stretch_wid=2, stretch_len=1)
        start_y = random.randint(-250, 250)
        self.goto(START_X, start_y)
        all_cars.append[self]

    def move(self):
        self.forward(MOVE_INCREMENT)
