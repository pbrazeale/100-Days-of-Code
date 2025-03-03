from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website_text = website_input.get()
    email_text = email_input.get()
    password_text = password_input.get()

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
