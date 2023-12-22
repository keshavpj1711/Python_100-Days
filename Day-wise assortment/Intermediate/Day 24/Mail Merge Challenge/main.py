# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hints for the code
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Reading the name list
with open("./Input/Names/invited_names.txt", "r") as names:
    names_list = names.readlines()  # Storing all the names as list items

# Reading the file
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    in_letter = letter.read()  # Storing the whole letter as a string

    # Stripping the names and replacing them with '[name]'
    for i in names_list:  # Traversing through the names_list to strip the names separately
        # Storing the stripped name
        name = i.strip()
        # Replacing [name] with name in letter_lines and storing the new letter in named_letter variable
        named_letter = in_letter.replace("[name]", name)

        # Finally writing the Output to a file name.txt
        with open(f"./Output/ReadyToSend/{name}.txt", "w") as letters_ready:
            letters_ready.write(named_letter)
            # We can do this in a single line
            # Since the named_letter has all the lines as a single string
