from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    password_list += [random.choice(symbols) for char in range(nr_letters)]
    password_list += [random.choice(letters) for char in range(nr_symbols)]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_input.insert(0, password)
    pyperclip.copy(password)
    #password_input.grid(column=2, row=4, columnspan=1)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_db():
    try:
        search_term = website_input.get()
        with open("data.json", "r") as DB:
            data = json.load(DB)
            print(data[search_term])
            messagebox.askokcancel(title="search_term",
                                   message=f"your login details for {search_term} are "
                                           f"\n username: {data[search_term]['email']}"
                                           f" \n Password: {data[search_term]['password']}")
    except FileNotFoundError:
        messagebox.askokcancel(title="Warning",
                               message=f"There is currently no data file present")
        print("no data file found")
    except KeyError:
        messagebox.askokcancel(title="Warning",
                               message=f"{website_input.get()} is not present in your Password database")
        print("entry not found")
    else:
        pass
    finally:
        pass

def add_entry():
    new_data = {
        website_input.get(): {
            "email": username_input.get(),
            "password": password_input.get()
        }
    }

    if len(username_input.get()) > 0 or len(website_input.get()) > 0 or len(password_input.get()) > 0:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are the deatils entered: \nemail: {username_input.get()} \nPassword: {password_input.get()} \n is it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as passworddb:
                    data = json.load(passworddb)
            except FileNotFoundError:
                with open("data.json", "w") as passworddb:
                    json.dump(new_data, passworddb, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as passworddb:
                    json.dump(data, passworddb, indent=4)
            finally:
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

password_input = Entry(width=35)
password_input.grid(column=2, row=4, columnspan=2)

# genorate password

genpassword_button = Button(text="Generate Password", command=generate_password)
genpassword_button.grid(column=3, row=4, columnspan=1)

# add entry to DB
add_entry = Button(text="Add", width=36, command=add_entry)
add_entry.grid(column=2, row=5, columnspan=2)

# search the DB
search = Button(text="Search", command=search_db)
search.grid(column=3, row=2, columnspan=1)

window.mainloop()
