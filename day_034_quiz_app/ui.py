from tkinter import *

THEME_COLOR = "#375362"

false_image = PhotoImage(file="/images/false.png")
true_image = PhotoImage(file="/images/true.png")


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.mainloop()
