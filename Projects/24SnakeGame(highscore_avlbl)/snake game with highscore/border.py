import turtle
from turtle import Turtle

# To use rgb 
turtle.colormode(255)

# Creating our border in the start of the game 
class Border(Turtle):

    def __init__(self):
        super().__init__("square")

        # Setting the color to mactch the theme
        self.color((67, 82, 61))

        # Our next target is to draw accross the border of screen
        
        # Initially we don't want to draw anything
        self.penup()
        self.pensize(width=5)
        # Moving to one corner to move 
        self.goto(345, 340) # at first corner
        self.pendown()
        self.goto(345, -365) # at second corner
        self.goto(-345, -365) # at second corner
        self.goto(-345, 340) # at third corner 
        self.goto(345, 340) # again at starting position
        self.hideturtle()
