# Importing required modules
from tkinter import *
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# Creating a dictionary to save the random word
random_word = {}


# ------------------------- TURNING CARDS -------------------------
def turn_card():
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(text_label, text="English", fill="white")
    canvas.itemconfig(text_word, text=random_word["English"], fill="white")


# ------------------------- CHANGING WORDS -------------------------
# Reading the csv file
data_file = pandas.read_csv("./data/1000_french_words.csv")
data_file_list = data_file.to_dict(orient="records")


# Defining a function to randomly change words in the text
def change_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data_file_list)
    # Changing the words in canvas
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(text_label, text="French", fill="black")
    canvas.itemconfig(text_word, text=random_word["French"], fill="black")
    # Flipping the cards
    flip_timer = window.after(3000, turn_card)


# ------------------------- CREATING UI -------------------------
# Configuring our window
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, turn_card)


# Creating canvas for cards
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# Setting up both the cards
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)
# Setting up the text
text_label = canvas.create_text(400, 185, font=("Arial", 40, "italic"), text="French")
text_word = canvas.create_text(400, 285, font=("Arial", 60, "bold"), text="")

# Creating buttons
# Initializing photos
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
# Creating right and wrong buttons
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=change_card)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=change_card)
wrong_button.grid(column=0, row=1)

# Now we also need to call the function beforehand
# Reason: to show a word when program first starts
change_card()

window.mainloop()
