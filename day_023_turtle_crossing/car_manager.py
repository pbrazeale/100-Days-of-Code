from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_X = 295


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.penup()
            car.left(180)
            car.shapesize(stretch_wid=1, stretch_len=2)
            start_y = random.randint(-250, 250)
            car.goto(START_X, start_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
