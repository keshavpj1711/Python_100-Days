# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hints for the code
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Reading the file
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    letter_lines = letter.readlines()  # Storing the lines as a list item

# Initialising a temp_var
letter_lines_with_name = []

# Reading the name list
with open("./Input/Names/invited_names.txt", "r") as names:
    names_list = names.readlines()  # Storing all the names as list items

# Stripping the names and replacing them with '[name]'
for i in names_list:  # Traversing through the names_list to strip the names separately
    letter_lines_with_name.append(letter_lines[0].replace("[name]", i.strip()))
    letter_lines_with_name.extend(letter_lines[1:])
    with open(f"./Output/ReadyToSend/{i.strip()}.txt", "w") as letters_ready:
        for k in letter_lines_with_name:
            letters_ready.write(k)

    # Setting the letter_lines_with_name = []
    letter_lines_with_name = []
