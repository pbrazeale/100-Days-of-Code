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
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.color(color)
        turtle.penup()
        turtle.goto(x=-240, y=y)
        racing_turtles.append(turtle)
        y += 60


def race():
    racing = True
    while racing:
        for turtle in racing_turtles:
            speed = random.randint(10, 40)
            turtle.forward(speed)

            if turtle.xcor() >= 250:
                winning_color = turtle.pencolor()
                print(f"{winning_color} won the race!")
                if winning_color == user_bet:
                    print("YOU WIN!")
                else:
                    print("You lose.")
                racing = False
                break


start_race()

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color:  "
)

race()

bye()
