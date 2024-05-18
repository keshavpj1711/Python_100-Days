# Stuff we need to make this app is 
    # Getting hold of api 
    # Next we need to revise Tkinter and 
    
from quiz_ques import GetQuestions
from quiz_brain import QuizBrain
from ui import QuizGUI

# Creating the respective obejcts to be used 
quiz_questions = GetQuestions().questions_list
quiz_brain = QuizBrain(quiz_questions)
quiz_ui = QuizGUI(quiz_brain)

# Basically loops till there are questions present in the data
# for i in range(0, len(quiz_questions)):
#     quiz_brain.next_question()
#     quiz_brain.check_answer()
#     quiz_brain.show_score()

# Our next target is to get everything to GUI and that too TKinter in Classes
