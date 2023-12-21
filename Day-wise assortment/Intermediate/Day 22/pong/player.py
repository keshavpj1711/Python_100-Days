from turtle import Turtle


class Player:
    def __init__(self):
        self.player = Turtle("square")
        self.player.shapesize(stretch_len=0.3, stretch_wid=4)
        self.player.penup()
        self.player.speed(0)

    def set_positions(self, player_number):
        if player_number == 1:
            self.player.goto(-425, 0)
        if player_number == 2:
            self.player.goto(425, 0)
        # self.player.speed(0)

    def up(self):
        if self.player.ycor() < 235:
            self.player.goto(self.player.xcor(), self.player.ycor()+40)

    def down(self):
        if self.player.ycor() > -235:
            self.player.goto(self.player.xcor(), self.player.ycor()-40)
