from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

    def score(self, out_of_bounds):
        if out_of_bounds == "right":
            left_score += 1
        elif out_of_bounds == "left":
            right_score += 1
