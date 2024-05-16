from turtle import Turtle, Screen


# Defining methods for movement for our turtle
def turn_clockwise():
    fury.right(10)


def turn_anticlockwise():
    fury.right(-10)


def move_forward():
    fury.forward(10)


def move_backward():
    fury.back(10)


# Defining some other actions of turtle and its screen like
# Getting turtle in the middle by pressing space
# Clearing the screen by pressing c
def clear_screen():
    fury.clear()
    fury.penup()
    fury.home()
    fury.pendown()
    

# Creating my turtle and screen
fury = Turtle()
screen = Screen()

# listen() function helps to listen for any incoming key press
screen.listen()

# All our keybindings for our game
screen.onkey(key="a", fun=turn_anticlockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="space", fun=clear_screen)

screen.exitonclick()
