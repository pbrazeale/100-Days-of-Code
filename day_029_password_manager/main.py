from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website_text = website_input.get()
    email_text = email_input.get()
    password_text = password_input.get()

    if len(website_text) > 0 and len(email_text) > 0 and len(password_text) > 0:
        is_okay = messagebox.askokcancel(
            title=website_text,
            message=f"These are the details entered: \nEmail: {email_text} \nPassword: {password_text} \nIs it okay to say?",
        )
    else:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!"
        )

    if is_okay:
        with open("password_log.txt", "a") as file:
            file.write(f"{website_text} | {email_text} | {password_text}\n")
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)

# Logo Row
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Row
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

# Email Row
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "test@test.com")

# Password Row
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(column=2, row=3)

# Add Password Row
add_password_btn = Button(text="Add", width=36, command=add_password)
add_password_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
