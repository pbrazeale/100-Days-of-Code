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
        with open("data.txt", "r+") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score_num}     High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def score(self):
        self.score_num += 1
        self.update_scoreboard()

    def reset(self):
        if self.score_num > self.high_score:
            self.high_score = self.score_num
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score_num = 0
        self.update_scoreboard()
