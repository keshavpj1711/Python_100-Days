# This is where we will get the response of the api
# Here we took the response and stored all the questions in questions[]

import requests
import html

class GetQuestions:
    
    def __init__(self):

        response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean")
        # For handling any error
        response.raise_for_status()

        # Getting the data 
        question_list = response.json()["results"]
        # print(question_list)

        self.questions_list = []

        # Looping thru question_list and populating questions with question and correct answer
        for i in range(0, len(question_list)):
            self.questions_list.append([html.unescape(question_list[i]["question"]), question_list[i]["correct_answer"]])
            # print(questions[i])