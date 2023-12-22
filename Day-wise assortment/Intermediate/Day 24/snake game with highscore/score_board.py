from turtle import Turtle

# Defining constants
ALIGNMENT = "center"
FONT_FOR_SCORE = ('Arial', 12, 'bold')
FONT_FOR_GAME_OVER = ('Arial', 12, 'bold')


# We can write using our turtle so that's what we are going to be using in this lesson
class ScoreBoard(Turtle):
    def __init__(self):
        self.score_count = 0

        # Opening file to take high score from text file
        with open("high_score.txt") as high_file:
            self.high_score = int(high_file.read())

        super().__init__()
        self.hideturtle()
        self.goto(0, 340)
        self.write(arg=f"Score: {self.score_count}", move=False, align=ALIGNMENT, font=FONT_FOR_SCORE)

    def increase_score(self):
        # Calling update_score to show the increased score
        self.update_score()

        # To increase the score here itself here rather than in main.py
        self.score_count += 1

    def update_score(self):
        self.clear()  # We have to clear after every score update to get rid of overlap
        self.write(arg=f"Score: {self.score_count} | HighScore: {self.high_score}", move=False, align="center",
                   font=('Arial', 14, 'bold'))

    def reset(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count

            # writing high score to file
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))

        # Resetting the score to zero for next player
        self.score_count = 0

        # Calling increase_score to display the score at the end
        self.update_score()

    # We commented this functionality out since we want to play game till we want
    # So that we can get a high score and have multiple chances
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT_FOR_GAME_OVER)

