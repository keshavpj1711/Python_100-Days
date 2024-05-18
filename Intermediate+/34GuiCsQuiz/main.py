# Stuff we need to make this app is 
    # Getting hold of api 
    # Next we need to revise Tkinter and 
    
from quiz_ques import GetQuestions
from quiz_brain import QuizBrain
import tkinter as tk

quiz_questions = GetQuestions().questions_list
quiz_brain = QuizBrain(quiz_questions)

for i in range(0, len(quiz_questions)):
    quiz_brain.next_question()
    quiz_brain.check_answer()
    quiz_brain.show_score()

