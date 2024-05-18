import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizGUI:

    def __init__(self, quiz_brain: QuizBrain):
        # By doing this: "quiz_brain: QuizBrain"
        # basically we define the data type of the parameter that we want
        self.quiz_brain = quiz_brain
        
        # Getting the TK window up and running
        self.window = tk.Tk()
        self.window.title("QuizApp")
        self.window.config(height=500, width=400)

        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        # Creating a Label for score
        self.score_label = tk.Label(text=f"Score:{self.quiz_brain.user_score}", font=("Arial", 15, "normal"), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=0, row=0)

        # Creating a canvas
        self.question_space = tk.Canvas(bg="white", height=250, width=300)
        self.question_text = self.question_space.create_text(150, 125, text="Question", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.question_space.grid(column=0, row=1, columnspan=2, pady=50)

        # Adding the two required buttons
        self.false_button = tk.Button(height=50, width=50, text="FALSE", highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(column=0, row=2) 
        self.true_button = tk.Button(height=50, width=50, text="TRUE", highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(column=1, row=2)

        # Calling next question
        self.get_next_question()

        self.window.mainloop()

    
    def get_next_question(self):

        if self.quiz_brain.question_number < 10: # According to indexing
            # Basically here we will also update the score everytime
            self.score_label.configure(text=f"Score:{self.quiz_brain.user_score}")

            q_text = self.quiz_brain.next_question()[0] 
            # Since this returns list with question at 0 as well as ans at 1 index

            # Changing text in canvas
            self.question_space.itemconfig(self.question_text, text=f"{q_text}")

        else:
            self.score_label.configure(text=f"Final Score:{self.quiz_brain.user_score}")

            self.question_space.itemconfig(self.question_text, text="Quiz Completed")

            # And next thing we want to do is disable those buttons
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def true_clicked(self):
        if self.quiz_brain.check_answer("T") == 1:
            self.flash_screen_color("light green")
        else:
            self.flash_screen_color("red")

    def false_clicked(self):
        if self.quiz_brain.check_answer("F") == 1:
            self.flash_screen_color("light green")
        else:
            self.flash_screen_color("red")

    def flash_screen_color(self, color_to_flash):
        self.question_space.configure(bg=f"{color_to_flash}")
        self.window.after(500, self.set_screen)

    # This function basically sets the screen for new question
    def set_screen(self):
        self.question_space.configure(bg="white")
        self.get_next_question()