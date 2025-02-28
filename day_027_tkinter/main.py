# import tkinter
from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_lable = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_lable.place(x=0, y=0)
my_lable.grid(column=0, row=0)
my_lable.config(padx=20, pady=20)
my_lable.config(text="New Text")


# Button
def button_clicked():
    label_title = input.get()
    my_lable.config(text=label_title)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="new button", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
