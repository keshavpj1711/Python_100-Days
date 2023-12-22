import time
import turtle
from turtle import Turtle

# Defining our constants
MOVE_DISTANCE = 10
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Setting color mode to 255
turtle.colormode(255)


# Our task here is to create a Snake class, which serve as a blueprint for our snake
# Also it should be able to move the snake once it's called
class Snake:
    def __init__(self):
        # Creating our snake
        self.snake = []
        # Calling create_snake to create our snake
        self.create_snake()
        # Since we are controlling most of the things with snake head so creating a variable for snake head
        self.snake_head = self.snake[0]

    def create_snake(self):
        # Adding body to our snake
        for positions in STARTING_POSITION:
            self.add_segment(positions)

    def add_segment(self, position_of_segment):
        new_segment = Turtle("square")
        self.snake.append(new_segment)  # Appending new segments to snake
        new_segment.color((67, 82, 61))  # Setting the color of our snake
        new_segment.penup()
        # Penup so that no lines are drawn on the movement of segments of our snake
        new_segment.goto(position_of_segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def reset_snake(self):
        # Hiding all the segments as they still linger around even after dying
        for i in self.snake:
            i.hideturtle()
        # Clearing all the segments
        self.snake.clear()
        # Calling create_snake to create our snake
        self.create_snake()
        # Since we are controlling most of the things with snake head so creating a variable for snake head
        self.snake_head = self.snake[0]

    def move(self):
        # This for loop actually moves the position of the last snake_segment to snake_segment just after it
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        # Now anything we do with the first segment all the other elements would follow since 2nd segment follows 1st
        self.snake_head.forward(MOVE_DISTANCE)

    # An important thing to note is that the head can't move on itself,
    # So when moving up snake can't move down similarly when moving right it can move left
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
