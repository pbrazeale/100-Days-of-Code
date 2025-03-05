from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn_dict = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn_dict = original_data.to_dict(orient="records")
else:
    to_learn_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict)
    current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="balck")
    canvas.itemconfig(card_word, text=current_card["French"], fill="balck")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn_dict.remove(current_card)
    pandas.DataFrame(to_learn_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# import images
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

# Create Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 273, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

# Language text
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))

# Word
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))


# buttons
wrong_btn = Button(
    image=wrong_image, highlightthickness=0, padx=50, pady=50, command=next_card
)
wrong_btn.grid(column=0, row=1)

right_btn = Button(
    image=right_image, highlightthickness=0, padx=50, pady=50, command=is_known
)
right_btn.grid(column=1, row=1)

next_card()

window.mainloop()
