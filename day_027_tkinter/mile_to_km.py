from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_int_label = Label(text="0")
km_int_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


def calculate():
    km_int = f"{float(miles_input.get()) * 1.609: .2f}"
    km_int_label.config(text=km_int)


calc_btn = Button(text="Calculate", command=calculate)
calc_btn.grid(column=1, row=2)

window.mainloop()
