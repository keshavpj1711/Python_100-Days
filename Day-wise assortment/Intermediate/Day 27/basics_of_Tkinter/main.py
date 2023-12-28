import tkinter as tk


# Defined functions
def button_clicked():
    # On executing this the user_input.get() gives us the text value in the entry
    my_label["text"] = f"{user_input.get()}"


# Creating our screen or say our window
window = tk.Tk()

# Naming the title
window.title("First GUI prog")

# Setting the min size of the screen
window.minsize(width=500, height=300)

# Adding a label
my_label = tk.Label(text="First Label", font=("Arial", 20, "normal"))
# The font= argument here works in the same way as that in turtle
# The packer function is used to place things on the screen
# It's like the geometry mechanism
my_label.pack(side="top")

# Now, as we know, how these **kwargs work,
# So, we can directly change the text in the label
my_label["text"] = "Changed the label"

# Creating a button
button = tk.Button(text="Click Me", command=button_clicked)
button.pack(side="top")
# Currently this button does nothing
# To make it functional we will make use of the command argument

# Creating an entry component to our program
user_input = tk.Entry(width=20)
user_input.pack()

# Keeping our windows open
# This is to be kept at the end of the program
tk.mainloop()

# In this file we have so far worked with
# window, window size
# label, packer method
# button and entry
