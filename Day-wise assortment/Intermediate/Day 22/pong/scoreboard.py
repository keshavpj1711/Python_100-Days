from turtle import Turtle

# Defining Constants
ALIGNMENT = "center"
FONT = ("Roboto", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.user1_score = 0
        self.user2_score = 0
        self.goto(0, 260)

    def exit_game(self):
        if self.user1_score > self.user2_score:
            self.goto(0, 0)
            self.write("Player1 Wins!!", align=ALIGNMENT, font=FONT)

        elif self.user2_score == self.user1_score:
            self.goto(0, 0)
            self.write("It's a Draw!!", align=ALIGNMENT, font=FONT)

        else:
            self.goto(0, 0)
            self.write("Player2 Wins!!", align=ALIGNMENT, font=FONT)

        return False

    def increase_score(self, player_no):
        if player_no == 1:
            self.user1_score += 1
        elif player_no == 2:
            self.user2_score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Player1: {self.user1_score} | Player2: {self.user2_score}", align=ALIGNMENT, font=FONT)
