import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)

# Label
my_lable = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_lable.pack(side="bottom")


window.mainloop()
