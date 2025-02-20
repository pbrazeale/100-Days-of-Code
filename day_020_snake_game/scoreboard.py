from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.score_num = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score_num}", align=ALIGNMENT, font=FONT)

    def score(self):
        self.score_num += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
