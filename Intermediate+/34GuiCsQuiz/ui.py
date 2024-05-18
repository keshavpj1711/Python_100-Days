import tkinter as tk

class QuizGUI:

    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("QuizApp")

        self.window.configure(bg="dark blue", padx=20, pady=20)

        # Creating a canvas
        self.question_space = tk.Canvas(bg="white", height=250, width=300)
        self.question_space.create_text(text="Question", font=)
        

        self.window.mainloop()