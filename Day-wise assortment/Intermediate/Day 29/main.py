from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# Setting up our window
window = Tk()
window.title("Tala Chabhi")  # Changing the title
window.config(padx=20, pady=20, bg="white")

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
email_username_entry = Entry(width=54, highlightcolor="dodgerblue", highlightthickness=1)
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=35, highlightcolor="dodgerblue", highlightthickness=1)
password_entry.grid(column=1, row=3)

# Creating our buttons
generate_button = Button(text="Generate Password", highlightthickness=0, bg="white", borderwidth=1, activebackground="dodgerblue", activeforeground="white")
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=46, highlightthickness=0, bg="white", borderwidth=1, activebackground="dodgerblue", activeforeground="white")
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
