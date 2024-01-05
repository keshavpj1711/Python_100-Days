# Importing required modules
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME1 = "Arial"
FONT_NAME2 = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# Creating our window
window = Tk()
window.config(padx=100, pady=100, bg=YELLOW)
window.title("Pomodoro")

# Creating canvas
# Setting the width and height same as that of image and making highlight thickness 0
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Adding image to canvas
tomato_img = PhotoImage(file="tomato.png")  # This class of tkinter is there to store image from its file location
canvas.create_image(100, 112, image=tomato_img)  # This image argument only takes an image in a certain way
# Creating text to be displayed on the tomato
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME1, 32, "bold"))
canvas.grid(column=1, row=1)

# Creating our timer label
timer_label = Label(text="Timer", font=(FONT_NAME2, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Creating our start button
start_button = Button(text="Start", bg="white", pady=5, padx=5)
start_button.grid(column=0, row=2)

# Creating our reset button
reset_button = Button(text="Reset", bg="white", pady=5, padx=5)
reset_button.grid(column=2, row=2)

# Creating our checkbox
checkbox = "✔"


window.mainloop()