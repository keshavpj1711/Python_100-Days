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
print(name)

# Creating a new dict with phonetics of the letters in given name
your_name_dict = {alpha: phonetics_dict[alpha] for alpha in name}
print(your_name_dict)
