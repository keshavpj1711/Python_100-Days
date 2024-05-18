# Here we will code the gui elements of the app 

class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.user_score = 0
        self.user_choice = ""
        self.current_question = [] 
        self.questions_remaining = len(question_list)
        # the data stored will be of format [question, correct answer]

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.q_text = self.current_question[0]
        self.q_ans = self.current_question[1]
        self.user_choice = input(f"Q{self.question_number+1}. {self.q_text} (T/F)?: ")
        self.question_number += 1
        self.questions_remaining -= 1

    def check_answer(self):
        if self.current_question[1][0] == self.user_choice:
            self.user_score += 1
        else:
            pass
    
    def show_score(self):
        print(f"Your score is ({self.user_score}/{len(self.question_list)})")