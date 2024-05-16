import time
from snake import Snake
from food import Food
from score_board import ScoreBoard
from border import Border
from turtle import Screen


# To exit the loop when we click escape key
def exit_loop():
    global game_is_on
    game_is_on = False


# Initializing screen
screen = Screen()
# We are using keyword arguments here so anyone reading it can easily understand
screen.setup(width=700, height=740)
# Changing the color mode to use rgb values
screen.colormode(255)
# Also note this is how we use rgb(x, x, x) values
# Setting bgcolor to the old school nokia screen
screen.bgcolor(199, 240, 215)
# Setting title of the screen
screen.title("Snake Game - Nokia 3310")
# Stoping the tracing
screen.tracer(0)

# Creating a border 
border = Border()
# Creating our snake
snake = Snake()
# Initializing food
food = Food()
# Initializing scoreboard
scoreboard = ScoreBoard()

# The problem that we faced was the animation of turtle not being proper when it moves,
# Since one turtle moves at a time.
# To fix this we used tracer() and update()
# if trace(0) it stops tracing the turtle

# Changing the direction of our snake
screen.listen()  # Listens for any keypress
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)

# Exiting the loop i.e., stopping the game
screen.onkeypress(key="Escape", fun=exit_loop)

# Flag which controls the flow of game
game_is_on = True

while game_is_on:
    screen.update()  # This updates the screen after all the segments have moved
    time.sleep(0.025)  # A small-time lag to control the speed of the snake
    # Using the move method in Snake() class to move our turtle continuously
    snake.move()

    # Detect collision
    if snake.snake_head.distance(food) < 13:
        food.refresh()
        # Extending the snake as it eats the food
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.snake_head.xcor() > 340 or snake.snake_head.xcor() < -340 or snake.snake_head.ycor() > 340 or snake.snake_head.ycor() < -360:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset_snake()

    # Detect collision with tail
    for segments in snake.snake[1:]:  # or we could have just used [1:] to get hold of list except the first element
        if snake.snake_head.distance(segments) < 7:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset_snake()


screen.exitonclick()
