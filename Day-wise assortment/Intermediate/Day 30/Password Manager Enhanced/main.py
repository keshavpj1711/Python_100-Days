from tkinter import *  # This only imports all the classes present in tkinter
# Now, to use messagebox which is just a module, we need to import it separately
from tkinter import messagebox
from password_generator import py_password_gen
import pyperclip  # This module is to achieve the copy and paste functionality
import json  # Importing json module to add and get data from json file
# Also we are making a change to saving the data
# Now we will be saving data in json file instead of txt file
# Reason being it's easier to work with data when it's in json rather than in txt file


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
            with open("database.json", "w") as database:
                json.dump(new_data, database)

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
website_entry = Entry(width=54, highlightcolor="dodgerblue", highlightthickness=1)
website_entry.grid(column=1, row=1, columnspan=2)
# Having the cursor already in the first entry
website_entry.focus()
email_username_entry = Entry(width=54, highlightcolor="dodgerblue", highlightthickness=1)
email_username_entry.grid(column=1, row=2, columnspan=2)
# Having some default email that you use frequently
email_username_entry.insert(0, "crueser123@gmail.com")
password_entry = Entry(width=35, highlightcolor="dodgerblue", highlightthickness=1)
password_entry.grid(column=1, row=3)

# Creating our buttons
generate_button = Button(text="Generate Password", highlightthickness=0, bg="white", borderwidth=1,
                         activebackground="dodgerblue", activeforeground="white", command=gen_pass)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=46, highlightthickness=0, bg="white", borderwidth=1,
                    activebackground="dodgerblue", activeforeground="white", command=save_details)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
