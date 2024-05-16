import random
from turtle import Turtle, Screen
import turtle

fury = Turtle()
fury.shape("turtle")
fury.color("dodgerblue1")
# color_list = ['firebrick1', 'dodgerblue1', 'mediumslateblue', 'coral', 'lightgreen', 'hotpink2', 'brown1',
# 'darkorchid1', 'seagreen1', 'lightsteelblue']


# Drawing a dashed line
# To draw a dashed line we can use up() and down() function
# for i in range(0,6):
#     fury.forward(10)
#     fury.up()
#     fury.forward(10)
#     fury.down()


# Drawing a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
# fury.width(2)
# for i in range(3,11):
#     for j in range(0,i):
#         fury.forward(100)
#         fury.right(360/i)
#     fury.color(color_list[random.randint(0, len(color_list)-1)])


# Generating a completely random colour,
# This can be done using rgb(x, x, x)
# Step 1: changing the colour mode
turtle.colormode(255)


# Step 2: generating 3 random integers
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


# Generating a random walk
# fury.width(10)
# fury.speed(0)
# for i in range(400):
#     fury.color(random_color())
#     choice = random.randint(1, 3)
#     if choice == 1:
#         fury.forward(25)
#     elif choice == 2:
#         fury.right(90)
#         fury.forward(25)
#     elif choice == 3:
#         fury.right(270)
#         fury.forward(25)


# Drawing a spinograph
fury.speed(0)
fury.width(2)
for i in range(0, 100):
    fury.circle(150)
    fury.right(360/100)
    fury.color(random_color())


screen = Screen()
screen.exitonclick()