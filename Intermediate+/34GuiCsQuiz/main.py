# Stuff we need to make this app is 
    # Getting hold of api 
    # Next we need to revise Tkinter and 
    
from quiz_ques import GetQuestions
from quiz_brain import QuizBrain
from ui import QuizGUI

# Creating the respective obejcts to be used 
quiz_questions = GetQuestions().questions_list

# Passing on the quiz_questions generated from the GetQuestions class
quiz_brain = QuizBrain(quiz_questions)

# Passing on the QuizBrain to quiz UI to further use it accordingly
quiz_ui = QuizGUI(quiz_brain) # From here mostly the quiz_ui takes control

# Our next target is to get everything to GUI and that too TKinter in Classes
