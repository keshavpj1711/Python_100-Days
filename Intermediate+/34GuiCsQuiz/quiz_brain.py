# Here we will code the gui elements of the app 

class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.user_score = 0
        self.user_choice = ""
        self.current_question = [] 
        # the data stored will be of format [question, correct answer]

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        # self.user_choice = # getting the choice via tkinter button
        self.question_number += 1

    def check_answer(self):
        if self.current_question[1][0] == self.user_choice:
            self.user_score += 1
        else:
            pass
    
    def show_score(self):
        # Calling function of gui to update the score
        pass