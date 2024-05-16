# Importing required modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Now our next goal is to create a question bank,
# But it should have question in the form of objects
question_bank = []
for i in range(0, len(question_data) - 1):
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))
    # Or for better readability what we can do is
    # question_text = question_data[i]["text"]
    # question_answer = question_data[i]["answer"]
    # new_question = Question(question_text, question_answer)
    # question_bank.append(new_question)

print(len(question_bank))
quiz = QuizBrain(question_bank)

while quiz.still_questions_remaining():
    quiz.next_question()
    quiz.check_correct()
    quiz. show_score()
