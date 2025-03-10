from tkinter import *

THEME_COLOR = "#375362"

false_image = PhotoImage(file="/images/false.png")
true_image = PhotoImage(file="/images/true.png")


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white")
        self.score_label.grid(row=0, column=1)

        self.window.mainloop()
