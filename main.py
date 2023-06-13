from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    pass
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)

padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=2, row=1)

#website label/ button

website_label = Label(text="Website")
website_label.grid(column=1, row=2)

website_input = Entry(width=35)
website_input.grid(column=2, row=2, columnspan=2)

#email/Username

username_label = Label(text="Email/Username:")
username_label.grid(column=1, row=3)

username_input = Entry(width=35)
username_input.grid(column=2, row=3, columnspan=2)

# password

password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

password_input = Entry(width=21)
password_input.grid(column=2, row=4, columnspan=1)

# genorate password

genpassword_button = Button(text="Generate Password", command=generate_password)
genpassword_button.grid(column=3, row=4, columnspan=1)

# add entry to DB
add_entry = Button(text="Add", width=36, command=add_entry)
add_entry.grid(column=2, row=5, columnspan=2)

window.mainloop()