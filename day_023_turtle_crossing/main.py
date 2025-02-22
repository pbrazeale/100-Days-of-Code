import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CARS = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if CARS < 20:
        car_manager.create_car()
        CARS += 1

    car_manager.move()


screen.exitonclick()
