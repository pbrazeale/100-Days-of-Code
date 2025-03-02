# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=600, height=600)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(300, 120, image=logo_img)
canvas.grid(column=1, row=0)


window.mainloop()
