import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
winner_turtle = ""

# Setting up the screen size
screen.setup(width=550, height=400)
# Now when building this game, it's very imp to set the screen size
# Because that's how we will be aligning our turtles for start and,
# Getting to know which turtle won

# List of colors
color_list = ['firebrick2', 'dodgerblue', 'lightgreen', 'hotpink', 'black']

# Placing the bet on one of the turtle
user_bet = screen.textinput(title="Place your bet",
                            prompt="Enter a color[firebrick2/dodgerblue/lightgreen/hotpink/black]: ")

# Getting our participants ready, giving them colors and setting there positions
turtle_list = []
y_coord = [-100, -50, 0, 50, 100]
for i in range(0, 5):
    turtle_list.append(Turtle("turtle"))
    turtle_list[i].color(color_list[i])
    turtle_list[i].penup()
    turtle_list[i].goto(-250, y_coord[i])

# Once we have our bet start race
if user_bet:
    is_race_on = True

while is_race_on:
    for i in range(0, 5):
        random_distance = random.randint(1, 10)
        turtle_list[i].forward(random_distance)
        if turtle_list[i].pos()[0] >= 250:  # Checking if the turtle touches the finish line or not
            winner_turtle = color_list[i]
            is_race_on = False  # Setting our flag false to stop the while loop
            break

# Finally printing results
if winner_turtle == user_bet:
    print("You Won!!")
else:
    print(f"You lose, winner is {winner_turtle}")