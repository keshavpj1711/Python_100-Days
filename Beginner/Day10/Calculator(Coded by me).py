# Importing req modules
import sys


# Defining the req functions
def add(num_1, num_2):
    """This function takes 2 numbers and adds them"""
    return num_1 + num_2


def subtract(num_1, num_2):
    """This function takes 2 numbers and subtracts them"""
    return num_1 - num_2


def multiply(num_1, num_2):
    """This function takes 2 numbers and multiplies them"""
    return num_1 * num_2


def divide(num_1, num_2):
    """This function takes 2 numbers and divide them"""
    if num_2 == 0:
        return "Not defined"
    return num_1 / num_2


# Some global variable that we will use for our program to work flawlessly
result = 0


# We defined the whole to be a function so that we can easily get to the start with the help of recursion
def calculator():
    global result
    print("Operations")
    print("+\n-\n*\n/")

    num1 = float(input("Enter your first number: "))

    while True:
        print(f"Operating on {round(num1, 2)}")
        operation = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        if operation == "+":
            result = add(num1, num2)
            print(f"Result = {round(result, 2)}")
        elif operation == "-":
            result = subtract(num1, num2)
            print(f"Result = {round(result, 2)}")
        elif operation == "*":
            result = multiply(num1, num2)
            print(f"Result = {round(result, 2)}")

        # For division, we need to be extra careful as division may result into undefined if num2 = 0
        elif operation == "/":
            result_division = divide(num1, num2)
            if result_division == "Not defined":
                print("You cant divide a number by zero")
                break
            else:
                result = result_division
            print(f"Result = {round(result, 2)}")
        else:
            print("Please enter a valid operation")
            continue

        # This loop is to just see the user chooses correct input in the continuation_choice
        while True:
            continuation_choice = input(f"Type 'y' to calculate with {round(result, 2)}, or type 'n' to start a new "
                                        f"calculation or 'e' to exit: ")
            if continuation_choice == 'y':
                num1 = result
                break
            elif continuation_choice == 'n':
                # To start the calculator once again we do it by again calling the calculator function
                calculator()
            # Below elif statement directly exits the program
            elif continuation_choice == 'e':
                sys.exit()
            else:
                print("Please enter a valid choice")
                continue


calculator()
