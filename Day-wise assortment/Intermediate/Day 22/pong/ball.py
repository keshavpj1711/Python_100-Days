from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.x_move = 5
        self.y_move = 5

    def move(self):
        # Increasing x and y cor to move the ball
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # Since we only need to change the y_direction of ball, thus we only changed self.y_move

    def bounce_x(self):
        self.x_move *= -1
        # When hitting the paddle, we need to change the x direction
