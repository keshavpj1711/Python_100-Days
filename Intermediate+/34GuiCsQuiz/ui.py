import tkinter as tk

THEME_COLOR = "#375362"

class QuizGUI:

    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("QuizApp")

        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        # Creating a Label for score
        self.score_label = tk.Label(text=f"Score:{0}", font=("Arial", 10, "normal"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=0, row=0)

        # Creating a canvas
        self.question_space = tk.Canvas(bg="white", height=250, width=300)
        self.question_text = self.question_space.create_text(150, 125, text="Question", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.question_space.grid(column=0, row=1, columnspan=2, pady=50)

        # Adding the two required buttons
        red_cross_img = tk.PhotoImage(file=r"./images/red_cross.png")
        green_tick_img = tk.PhotoImage(file=r"./images/green_tick.png")
        self.false_button = tk.Button(height=50, width=50, image=red_cross_img, highlightthickness=0)
        self.false_button.grid(column=0, row=2) 
        self.true_button = tk.Button(height=50, width=50, image=green_tick_img, highlightthickness=0)
        self.true_button.grid(column=1, row=2)

        self.window.mainloop()