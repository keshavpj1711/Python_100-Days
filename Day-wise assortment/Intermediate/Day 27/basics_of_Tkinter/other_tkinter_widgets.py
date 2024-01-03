import tkinter as tk


# Creating the window
window = tk.Tk()
# Adjusting the min size of the window
window.minsize(width=500, height=300)


# Creating entries
entry = tk.Entry(width=27)
# Adding text to begin with
entry.insert(tk.END, string="Some text to begin with")
# tk.END is a special constant value that represents the position just after the last character
# in the current text of the Entry widget.# Getting text in entry
print(entry.get())
entry.pack()


# Adding a textbox
text = tk.Text(height=5, width=20)
# Getting some text to begin with
text.insert(tk.END, "This is some initial text in the Text widget.")
# putting the cursor in textbox
text.focus()
# Displays the text in the window
text.pack()


# Creating a Spinbox
# Creating a function to print the input in spinbox
def spinbox_used():
    # Gets the current value in spinbox
    print(spinbox.get())


spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# Displaying it
spinbox.pack()


# Creating a scale
def scale_used(value):
    # Getting the current scale value
    print(value)


scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Creating a checkbox
def checkbutton_used():
    # Prints 1 if on button checked,
    # otherwise 0
    print(checked_state.get())
    # get() Retrieves the value of a certain attribute or property from an object or data structure
    # Uses include
    # getting value of a key in dictionary
    # fetching the input from tkinter text and entry widgets


# This variable is used to hold the checked state whether it's 1 or 0
checked_state = tk.IntVar()
checkbox = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbox.pack()


# Radiobuttons
def radio_used():
    print(radio_state.get())


# This is a variable to hold which radiobutton is checked
radio_state = tk.IntVar()
radio_button1 = tk.Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radio_button2 = tk.Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = tk.Listbox(height=4)
fruits = ["Apple", "Banana", "Orange", "Mango"]
# Adding items in listbox
for item in fruits:
    listbox.insert(fruits.index(item), item)  # Gets the index where the item is to be placed

# This is event binding
# Binds the listbox_used() function to the <<ListboxSelect>> event, which is triggered when an item is selected

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


tk.mainloop()
