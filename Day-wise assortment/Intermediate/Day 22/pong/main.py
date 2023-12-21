import time
from turtle import Screen
from player import Player
from ball import Ball

# Step 1: is initializing the screen
screen = Screen()
# Setting the screen width and height
screen.setup(width=900, height=600)
# Setting up the color
screen.bgcolor("gray80")

# Step 2: Initialising players
player_1 = Player()
player_2 = Player()

# Setting positions of player
player_1.set_positions(1)
player_2.set_positions(2)

# Setting up the controlling of players
screen.listen()
# Controlling player 1
screen.onkeypress(key="w", fun=player_1.up)
screen.onkeypress(key="s", fun=player_1.down)
# Controlling player 2
screen.onkeypress(key="Up", fun=player_2.up)
screen.onkeypress(key="Down", fun=player_2.down)

# Step 3: Creating ball
ball = Ball()

# Turning our game on
game_is_on = True
while game_is_on:
    ball.move()

    # Detect collision with upper and lower wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # Detect collision with paddle
    # For player 2
    if ball.xcor() > 415 and ball.distance(player_2.player) < 50:
        ball.bounce_x()
    # For player 1
    if ball.xcor() < -415 and ball.distance(player_1.player) < 50:
        ball.bounce_x()

    # Detecting if the ball has moved beyond player
    if ball.xcor() > 425 or ball.xcor() < -425:
        game_is_on = False

screen.exitonclick()
