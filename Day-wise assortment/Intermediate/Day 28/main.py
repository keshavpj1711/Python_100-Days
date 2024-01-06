# Importing required modules
import math
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
def start_timer():
    # Calling count_down()
    count_down(100)


def reset_timer():
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# One way we might approach is via importing time module
# What we can do is have some kind of counter and run a while loop
# with sleep(1) then we could count -= 1
# But the problem with this kind of approach is that,
# Once this loop is running we can have the event listening functionality also,
# our program won't be able to refresh, since till the while loop runs we won't be able to
# reach till window.mainloop()
# This window.mainloop is responsible for refreshing our window every mili-second and thus, our program will not run

# Coming up with another solution
# to tackle this problem, tkinter already has a built-in method window.after()
# what this does is after a certain mili-seconds we can call a program
def count_down(count):
    print(count)
    # timer_text["text"] = f"{count}" this method doesn't work if you are working with a canvas widget
    # To work with canvas elements

    # Configuring the look of the timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Using the dynamically typed functionality of python
    if count_sec == 0:
        count_sec = "00"

    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)  # This count-1 is passed on to count_down()


# ---------------------------- UI SETUP ------------------------------- #

# Creating our window
window = Tk()
window.config(padx=50, pady=50, bg=YELLOW)
window.title("Pomodoro")

# Creating canvas
# Setting the width and height same as that of image and making highlight thickness 0
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0, )
# Adding image to canvas
tomato_img = PhotoImage(file="tomato.png")  # This class of tkinter is there to store image from its file location
canvas.create_image(100, 112, image=tomato_img)  # This image argument only takes an image in a certain way
# Creating text to be displayed on the tomato
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME1, 32, "bold"))
canvas.grid(column=1, row=1)

# Creating our timer label
timer_label = Label(text="Timer", font=(FONT_NAME2, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Creating our start button
start_button = Button(text="Start", bg="white", pady=5, padx=5, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Creating our reset button
reset_button = Button(text="Reset", bg="white", pady=5, padx=5, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Creating our checkbox
checkbox = "✔"
check_marks = Label(text=checkbox, fg=GREEN, bg=YELLOW, font=(FONT_NAME2, 15, "bold"), pady=10)
check_marks.grid(column=1, row=3)

window.mainloop()
