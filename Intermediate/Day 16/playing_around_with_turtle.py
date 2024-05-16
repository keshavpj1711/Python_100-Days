# Importing the module
import turtle
import random

# Taping into the class Turtle present in turtle module
# Also to create an object we need to put parentheses after it,
# So now we have created an object and stored in under fury

fury = turtle.Turtle()
fury.shape("turtle")  # Changes the shape of the pointer
fury.color("mediumslateblue")

color_list = ['red', 'blue', 'mediumslateblue', 'coral', 'gold', 'hotpink', 'limegreen', 'orange', 'seagreen1']

# Moving the turtle to make interesting shape
n = int(input("Enter the number of times to create the shape: "))
for i in range(1, n+1):
    fury.forward(10*i)
    fury.right(90)
    fury.forward(20*i)
    fury.right(90)
    fury.forward(10*i)
    fury.color(color_list[random.randint(0, len(color_list)-1)])

my_screen = turtle.Screen()
print(fury)
print(my_screen.canvheight)  # Prints the canvas height
my_screen.exitonclick()  # This function does as it says
