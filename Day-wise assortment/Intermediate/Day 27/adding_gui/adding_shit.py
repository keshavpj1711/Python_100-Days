# Importing required modules
from tkinter import *


# Creating our window
window = Tk()
window.minsize(width=200, height=100)
window.config(padx=30, pady=30)

# Taking Entry for addition
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Creating Label for miles
miles = Label(text="Miles", font=("Arial", 10, "normal"))
miles.grid(column=2, row=0)

# Creating label is_equal_to
is_equal_to = Label(text="is equal to", font=("Arial", 10, "normal"))
is_equal_to.grid(column=0, row=1, padx=10)

# Creating another label which outputs the answer
km_conv = "hi" # 1.6*(float(entry.get()))
km = Label(text=f"{km_conv}", font=("Arial", 10, "normal"))
km.grid(column=1, row=1)

# Creating a label to display km_text
km_text = Label(text="km", font=("Arial", 10, "normal"))
km_text.grid(column=2, row=1)

# Adding a button to calculate
calc_button = Button(text="Calculate")
calc_button.grid(column=1, row=2)


window.mainloop()
