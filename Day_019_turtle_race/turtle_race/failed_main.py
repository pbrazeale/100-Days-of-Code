from turtle import Turtle, Screen, bye
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


# tim = Turtle(shape="turtle")
# tim.color("blue")
# tim.penup()
# tim.goto(x=-240, y=-194)

racing_turtles = []


def start_race():
    y = -150
    for _ in range(len(colors)):
        name = str(colors[_])
        racing_turtles.append(name)
        name = Turtle(shape="turtle")
        name.color(colors[_])
        name.penup()
        name.goto(x=-240, y=y)
        y += 60


def race():
    racing = True
    while racing:
        for _ in range(len(racing_turtles)):
            name = racing_turtles[_]
            speed = random.randint(10, 40)
            name.forward(speed)
            win_check = name.pos()[0]
            if win_check >= 250:
                print(f"{name} won the race!")
                if name == user_bet:
                    print("YOU WIN!")
                else:
                    print("You lose.")
                racing = False


start_race()

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color:  "
)

race()

bye()
