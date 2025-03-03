from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# import images
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

# Create Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 273, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

# Language text
canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))

# Word
canvas.create_text(400, 263, text="Testing", font=("Arial", 60, "bold"))


# buttons
wrong_btn = Button(image=wrong_image, highlightthickness=0, padx=50, pady=50)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right_image, highlightthickness=0, padx=50, pady=50)
right_btn.grid(column=1, row=1)

window.mainloop()
