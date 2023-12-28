import tkinter as tk

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
my_label.pack(expand=True)

# Keeping our windows open
# This is to be kept at the end of the program
tk.mainloop()
