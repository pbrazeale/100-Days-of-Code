# import tkinter
from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

# Label
my_lable = Label(text="I am a label", font=("Arial", 24, "bold"))
my_lable.pack()
my_lable.config(text="New Text")


# Button
def button_clicked():
    label_title = input.get()
    my_lable.config(text=label_title)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

window.mainloop()
