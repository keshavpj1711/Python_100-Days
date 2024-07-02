from flask import Flask
import random

COUNTDOWN = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXJpNmFkMWJvamx0bGljZ2Zxb2FiYWI3cGZyNWQ0ZjN4ejdiamN3ZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IsfrRWvbUdRny/giphy.webp"
TOOHIGH = "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmNobGluOHVkYXphbWdjOGJ3YWRjYjZybjB0bno1OXpkaXZtMDN0ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3xz2Bxn3qapMDKX8SA/giphy.webp"
TOOLOW = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmVqMjYyNDFqeWZjdDFsaDM4M2tmamhicWd5Yjh2bHBkNm1ydTR4YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IevhwxTcTgNlaaim73/giphy.webp"
WIN = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWpuMGpsNTZpMmd5MGJvaTc5aHJhbng1cDd1YjllNXM1aHo1c2gxcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eoxomXXVL2S0E/giphy.webp"

app = Flask(__name__)

# def make_heading(function):
#     def wrapper():
#         return f"<h1>{function()}</h1>"

#     return wrapper

@app.route('/')
def start_screen():
    return "<h1>Guess the number between 0 and 1</h1>"\
        f"<img src={COUNTDOWN}></img>"

# Logic for our game 
final_ans = random.randint(0,9)

@app.route('/<int:user_ans>')
def check_if_win(user_ans):
    if user_ans > final_ans:
        return "<h1>TOO HIGH</h1>"\
        f"<img src={TOOHIGH}></img>"
    elif user_ans < final_ans:
        return "<h1>TOO LOW</h1>"\
        f"<img src={TOOLOW}></img>"
    
    return "<h1>YEAHH!! YOU WIN</h1>"\
    f"<img src={WIN}></img>"

if __name__ == "__main__":
    app.run(debug=True)