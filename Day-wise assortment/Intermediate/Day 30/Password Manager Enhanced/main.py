from tkinter import *  # This only imports all the classes present in tkinter
# Now, to use messagebox which is just a module, we need to import it separately
from tkinter import messagebox
from password_generator import py_password_gen
import pyperclip  # This module is to achieve the copy and paste functionality
import json  # Importing json module to add and get data from json file


# Also we are making a change to saving the data
# Now we will be saving data in json file instead of txt file
# Reason being it's easier to work with data when it's in json rather than in txt file
# One problem which arises due to data storage in json file type is
# We can't enter two accounts for same website name, the reason being since the data is of dictionary type and,
# we can't have two keys having the same name


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():
    email = None
    password = None
    try:
        with open("database.json", "r") as database:
            data = json.load(database)
            email = data[f"{website_entry.get()}"]["email"]
            password = data[f"{website_entry.get()}"]["password"]

        messagebox.showinfo(title=f"{website_entry.get()}", message=f"Email: {email}\nPassword: {password}")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Database not created, add at least one account")

    except KeyError:
        messagebox.showerror(title="Error", message="No accounts found for this website")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    password_obj = py_password_gen.PasswordGen()
    password = password_obj.generate_password()
    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# Saving our details in database.txt
def save_details():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    is_filled = True
    # Creating a dictionary to be saved to database.json
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # Checking if any of the fields is empty:
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
        is_filled = False

    else:
        if is_filled:

            try:
                # One problem we might face is if the file is not there
                # We will encounter a file not found error
                # Another one is if a person types in a website name which is not in the database
                # We will encounter a key error
                with open("database.json", "r") as database:
                    # Reading the data from data
                    data = json.load(database)
                    # Updating the old data with new data
                    data.update(new_data)

            except FileNotFoundError:
                with open("database.json", "w") as database:
                    json.dump(new_data, database, indent=4)

            else:
                with open("database.json", "w") as database:
                    # Saving the data
                    json.dump(data, database, indent=4)
                    # Working of indent:

            finally:
                # Clearing previous entries after adding to files
                website_entry.delete(0, END)
                password_entry.delete(0, END)

        else:
            return None


# ---------------------------- UI SETUP ------------------------------- #

# Setting up our window
window = Tk()
window.title("Tala Chabhi")  # Changing the title
window.config(padx=50, pady=50, bg="white")

# Creating canvas for our image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
# Getting the image in logo_tala_chabhi var
logo_tala_chabhi = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_tala_chabhi)
canvas.grid(column=1, row=0)

# Creating our labels
website_label = Label(text="Website:", pady=5, bg="white")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:", pady=3, bg="white")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", pady=5, bg="white")
password_label.grid(column=0, row=3)

# Creating our entries
website_entry = Entry(width=35, highlightcolor="dodgerblue", highlightthickness=1)
website_entry.grid(column=1, row=1, columnspan=1)
# Having the cursor already in the first entry
website_entry.focus()
email_username_entry = Entry(width=54, highlightcolor="dodgerblue", highlightthickness=1)
email_username_entry.grid(column=1, row=2, columnspan=2)
# Having some default email that you use frequently
email_username_entry.insert(0, "crueser123@gmail.com")
password_entry = Entry(width=35, highlightcolor="dodgerblue", highlightthickness=1)
password_entry.grid(column=1, row=3)

# Creating our buttons
search_button = Button(text="Search", highlightthickness=0, bg="white", borderwidth=1,
                       activebackground="dodgerblue", activeforeground="white", width=14, command=search)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", highlightthickness=0, bg="white", borderwidth=1,
                         activebackground="dodgerblue", activeforeground="white", command=gen_pass)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=46, highlightthickness=0, bg="white", borderwidth=1,
                    activebackground="dodgerblue", activeforeground="white", command=save_details)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
