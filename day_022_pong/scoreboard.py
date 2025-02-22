from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"{self.left_score}  |  {self.right_score}", align=ALIGNMENT, font=FONT
        )

    def score(self, out_of_bounds):
        if out_of_bounds == "right":
            self.left_score += 1
            self.clear()
            self.update_scoreboard()

        elif out_of_bounds == "left":
            self.right_score += 1
            self.update_scoreboard()
