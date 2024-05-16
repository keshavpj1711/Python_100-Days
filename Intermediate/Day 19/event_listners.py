from turtle import Turtle, Screen


def move_forward():
    fury.forward(5)


fury = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key="space", fun=move_forward)  # This function here is an example of a higher order function
screen.exitonclick()


