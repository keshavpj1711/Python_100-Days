import random
import turtle
from turtle import Turtle, Screen


def random_color():
    color_list = [(58, 105, 148), (222, 234, 229), (225, 202, 110), (133, 85, 57), (220, 147, 74),
                  (231, 224, 203), (143, 178, 201), (195, 145, 171), (235, 221, 231), (141, 78, 102), (212, 90, 65),
                  (135, 181, 137), (64, 109, 91), (188, 82, 119), (151, 134, 66), (64, 157, 95), (43, 156, 190),
                  (183, 191, 202), (216, 176, 191), (108, 121, 157), (7, 58, 104), (13, 68, 123), (156, 28, 38),
                  (231, 174, 163), (173, 202, 183), (158, 203, 215), (174, 24, 17), (73, 57, 40), (78, 65, 46),
                  (41, 63, 58), (49, 76, 65)]
    any_color = random.choice(color_list)
    r = any_color[0]
    g = any_color[1]
    b = any_color[2]
    rgb = (r, g, b)
    return rgb


# The below code is just to extract the color list
# import colorgram
#
# colors = colorgram.extract('images.jpg', 36)
# rgb_colors = []
#
# # To get an idea what you can do is first look at how data is stored in you color list
# # for i in colors:
# #     print(i)
#
# for i in colors:
#     rgb = i.rgb
#     tuple_for_color = (rgb[0], rgb[1], rgb[2])
#     rgb_colors.append(tuple_for_color)
#
# print(rgb_colors)


# Defining our turtle
fury = Turtle()

# Setting the color mode
turtle.colormode(255)
fury.hideturtle()
fury.speed(0)

# Getting the turtle in a suitable position so that it draws in visible space
fury.penup()
fury.setheading(220)
fury.forward(310)
fury.setheading(0)

# Creating a loop
# Logic for when to turn
count = 0
for j in range(0, 10):
    for i in range(0,9):
        fury.dot(20, random_color())
        fury.penup()
        fury.forward(50)
    fury.dot(20, random_color())
    if count % 2 == 0:
        fury.setheading(90)
        fury.forward(50)
        fury.setheading(180)
        count += 1
    else:
        fury.setheading(90)
        fury.forward(50)
        fury.setheading(0)
        count += 1



screen = Screen()
screen.exitonclick()