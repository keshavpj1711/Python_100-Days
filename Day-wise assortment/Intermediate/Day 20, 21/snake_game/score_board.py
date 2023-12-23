from turtle import Turtle

# Defining constants
ALIGNMENT = "center"
FONT_FOR_SCORE = ('Arial', 12, 'bold')
FONT_FOR_GAME_OVER = ('Arial', 12, 'bold')


# We can write using our turtle so that's what we are going to be using in this lesson
class ScoreBoard(Turtle):
    def __init__(self):
        self.score_count = 0
        super().__init__()
        self.hideturtle()
        self.goto(0, 340)
        self.write(arg=f"Score: {self.score_count}", move=False, align=ALIGNMENT, font=FONT_FOR_SCORE)

    def increase_score(self):
        self.clear()  # We have to clear after every score update to get rid of overlap
        self.write(arg=f"Score: {self.score_count}", move=False, align="center", font=('Arial', 14, 'bold'))
        # To increase the score here itself here rather than in learning_csv_module.py
        self.score_count += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT_FOR_GAME_OVER)