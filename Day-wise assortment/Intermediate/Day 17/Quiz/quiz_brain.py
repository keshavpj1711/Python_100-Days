# Functions of this class is to:
# Asking the questions
# Checking if the answer was correct
# Checking if we are at the end of the quiz

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.user_score = 0
        self.question_list = question_list
        self.user_choice = ""

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.user_choice = input(f"Q{self.question_number+1} {current_question.q_text} (T/F)?: ")
        self.question_number += 1

    def still_questions_remaining(self):
        if self.question_number == len(self.question_list) - 1:
            return False
        else:
            return True

    def check_correct(self):
        current_question = self.question_list[self.question_number]
        if self.user_choice == current_question.q_answer[0]:
            self.user_score += 1
        else:
            pass

    def show_score(self):
        print(f"Your score: ({self.user_score}/{len(self.question_list)})")
