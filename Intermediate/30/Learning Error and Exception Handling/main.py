# Getting started with try and except block
try:
    demo_list = [32, 13, 56, 6]
    demo_dict = {"key": "value"}
    # print(demo_list[4])
    # print(demo_dict["key1"])

except IndexError as index_error_msg:
    # One thing to note is that as soon as the first error comes it executes the respective error block
    # So in this case as soon as the index error is detected it does not execute the line after that
    print("The index no is not present")
    print(f"Error message: {index_error_msg}")

except KeyError as key_error_msg:
    print("No such key present")
    print(f"Error message: {key_error_msg}")

# What is else block? if no exceptions are thrown in try block the else block is executed
else:
    print("Zero errors!!")

# Finally: this block runs no matter what happens
finally:
    # Raising your own errors
    # To do this we use the keyword raise followed by the error_code("and the error message")
    # raise TypeError("This is a error message")
    # Now to see when can this raising our own exceptions be helpful
    # To get an example checkout raising_exceptions.py

    print("Program execution completed")

# Doubt: One thing to note is that,
# The error message prints on the screen even before the else block
# Like this:
# Traceback (most recent call last):
#   File "D:\My Journey\Python - Road to Heaven\Day-wise assortment\Intermediate\Day 30\main.py", line 26, in <module>
#     raise TypeError("This is a error message")
# TypeError: This is a error message
# Zero errors!!

