# In this we will be creating a function which uses .title() function to change first letter of your name to uppercase
def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"


# Input
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
formatted_name = format_name(fname, lname)
print(f"Formatted Name: {formatted_name}")