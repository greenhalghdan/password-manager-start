from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    if len(username_input.get()) > 0 and len(website_input.get()) > 0 and len(password_input.get()) > 0:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the deatils entered: \nemail: {username_input.get()} \nPassword: {password_input.get()} \n is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as passworddb:
                passworddb.write(f"{website_input.get()} | {username_input.get()} | {password_input.get()}\n")
                website_input.delete(0, "end")
                password_input.delete(0, "end")
    else:
        messagebox.showinfo(title="Validation Error", message="You have not filled in all values")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)

padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=2, row=1)

#website label/ button

website_label = Label(text="Website")
website_label.grid(column=1, row=2)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=2, row=2, columnspan=2)

#email/Username

username_label = Label(text="Email/Username:")

username_label.grid(column=1, row=3)

username_input = Entry(width=35)
username_input.insert(0, "email@domain.com")
username_input.grid(column=2, row=3, columnspan=2)

# password

password_label = Label(text="Password:")
password_label.grid(column=1, row=4)

password_input = Entry(width=21)
password_input.grid(column=2, row=4, columnspan=1, )

# genorate password

genpassword_button = Button(text="Generate Password", command=generate_password)
genpassword_button.grid(column=3, row=4, columnspan=1)

# add entry to DB
add_entry = Button(text="Add", width=36, command=add_entry)
add_entry.grid(column=2, row=5, columnspan=2)

window.mainloop()
