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
text = tk.Text(height=10, width=20)
# Getting some text to begin with
text.insert(tk.END, "This is some initial text in the Text widget.")
# putting the cursor in textbox
text.focus()
# Displays the text in the window
text.pack()


tk.mainloop()
