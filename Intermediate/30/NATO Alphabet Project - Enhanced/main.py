# First, read the csv file using pandas
# Second, create a dictionary with alphabets as key and phonetics as values
# Taking input of the user
# Giving a clear output


# Importing req modules
import pandas

# Reading the csv
phonetics_data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Storing the data in a dictionary
phonetics_dict = {row.letter: row.code for (index, row) in phonetics_data.iterrows()}
print(phonetics_dict)

# Taking input from the user
name = (input("Enter your name: ")).upper()
name = name.replace(" ", "")  # To remove any whitespaces to avoid any error in your_name_dict
# print(name)

# Creating a new dict with phonetics of the letters in given name
# your_name_dict = {alpha: phonetics_dict[alpha] for alpha in name}
# print(your_name_dict)

# The first problem with the code is
# The code uses a dictionary comprehension to create your_name_dict.
# Dictionaries inherently store unique keys, meaning only one instance of each key (alpha) is retained,
# even if it appears multiple times in name.
# This explains why repeated letters like "A" in "AMAN" are only represented once.

# The solution:
# your_name_phonetics = [phonetics_dict[alpha] for alpha in name]
# print(your_name_phonetics)

# The second problem with the code is that when we input something that is not present in the dictionary
# Like numbers or special characters then it throws a key error

# The solution: Use of try and except block
while True:
    try:
        your_name_phonetics = [phonetics_dict[alpha] for alpha in name]
    except KeyError:
        print("Please Enter a valid name")
        name = (input("Enter your name: ")).upper()
        name = name.replace(" ", "")  # To remove any whitespaces to avoid any error in your_name_dict
    else:
        print(your_name_phonetics)
        break
