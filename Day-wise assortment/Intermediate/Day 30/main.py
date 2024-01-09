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
    print("Program execution completed")
