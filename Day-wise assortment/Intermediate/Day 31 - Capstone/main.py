# Importing required modules
from tkinter import *

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------- CREATING UI -------------------------
# Configuring our window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Creating canvas for cards
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# Setting up both the cards
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
# Setting up the text
french_label = canvas.create_text(400, 185, font=("Arial", 40, "italic"), text="French")
french_word = canvas.create_text(400, 285, font=("Arial", 60, "bold"), text="french word")

# Creating buttons
# Initializing photos
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
# Creating right and wrong buttons
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=0, row=1)

window.mainloop()
