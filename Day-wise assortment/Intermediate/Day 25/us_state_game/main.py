import turtle as tt
import pandas as pd

# This function is to get the coordinates of the mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
# Getting the coordinates of the mouse click
# tt.onscreenclick(get_mouse_click_coor)
# But we are not going to need it as we already have the coordinates in the csv file

# Configuring screen
screen = tt.Screen()
# Setting up the title of the screen
screen.title("U.S. States Game")
# Adjusting screen size wrt image size
screen.setup(width=800, height=600)
screen.bgpic("blank_states_img.gif")

# Hiding the turtle
tt.penup()
tt.hideturtle()

# # Note the image we are using is of .gif format because,
# # turtle is most compatible with .gif format
# image = "blank_states_img.gif"
# # Adding image as a shape to be used as a turtle shape
# screen.addshape(image)
#
# # Setting the turtle shape to image
# tt.shape(image)

# Reading the csv data
states_data = pd.read_csv("50_states.csv")
states_name_list = list(states_data["state"])

# Creating a dictionary to save both name and coords
states_dict = {}
for i in range(0, len(states_data.x)):
    states_dict[states_data.state[i]] = (states_data.x[i], states_data.y[i])
# print(states_dict)

# A list to store correct user_inputs
user_input_list = []

# A flag to keep track whether while loop run or not
game_is_on = True

while game_is_on:
    # Taking input from user
    user_input = screen.textinput(prompt="Name another state", title=f"({len(user_input_list)}/50)Guess the State")
    print(user_input)

    # Checking whether user_input is correct or not
    if user_input in states_name_list:
        if user_input in user_input_list:  # Checking if the user has already guessed the state
            print("Guessed already")
        else:
            # Placing the word in image
            x_cor = states_dict[user_input][0]
            y_cor = states_dict[user_input][1]
            tt.goto(x_cor, y_cor)  # Going to the coords
            tt.write(arg=f"{user_input}", align="center", font=("Arial", 8, "normal"))
            tt.goto(0, 0)  # Again bringing back the turtle to origin

            user_input_list.append(user_input)

    else:
        print("Naah!! Wrong")

    # As soon as user guesses all 50-states exit the loop
    if len(user_input_list) == 50:
        game_is_on = False

    # typing exit to exit out of loop
    if user_input == 'exit':
        game_is_on = False

# This keeps the program ON
screen.exitonclick()

# # Angela used to filter the coords by doing
# coords_data = states_data[states_data.state == user_input]
# # The coords can be accessed by
# x_coord = coords_data.x
# y_coord = coords_data.y
# # Then we could ask the turtle to go at given coords
