import turtle
from turtle import Turtle
import random

# Setting the colormode to 255 so that we can use rgb
turtle.colormode(255)


# Now the food that we will be creating will be a turtle itself
# Also we need our Food class to have all the capabilities of the Turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color((67, 82, 61))
        # Now since we want to have our food of size 10x10, therefore we scale accordingly
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        # Increasing the speed of turtle so that we don't have to see it being created in the center and then moving
        self.speed(0)

    # We want to change the location of food everytime snake eats it
    def refresh(self):
        random_x = random.randint(-335, 335)
        random_y = random.randint(-355, 335)
        self.goto(random_x, random_y)
