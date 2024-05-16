# To open and read the content of your files
file = open("my_file.txt")
contents = file.read()
file.close()
# The print statement outputs your file content
print(contents)

# To separate the outputs
print("\nMethod 1 to open file completed\n")

# Now many times we work with a file and forget to close it
# For this we can use a different method to open a file
with open("my_file.txt", mode='a') as file:
    file.write("\nA line added using write method")
    # contents = file.read()
    # print(contents)
# What this 'with' does is as soon as we are done using the file it closes the file
