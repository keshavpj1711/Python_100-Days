# Importing req modules
import random
import re

# Generating a list of letters
letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
letters_list = re.split(' ', letters)
# print(letters_list)

# Generating a list of symbols
symbols = "# ! $ % & ( ) * +"
symbols_list = re.split(' ', symbols)
# print(symbols_list)

# Generating list of numbers
nums = "0 9 8 7 6 5 4 3 2 1"
nums_list = re.split(' ', nums)


# print(nums_list)

class PasswordGen:

    def __init__(self):
        self.num_of_letters = random.randint(8, 10)
        self.num_of_symbol = random.randint(2, 4)
        self.num_of_numbers = random.randint(2, 4)

        self.total_len = self.num_of_symbol + self.num_of_numbers + self.num_of_letters

        self.Your_password = ""

    def generate_password(self):
        # Doing the easy level
        # letterssymbolnumbers

        # Easy Level

        for i in range(0, self.num_of_letters):
            # rand_int = random.randint(0, len(gen.letters_list)-1)
            # Your_password += gen.letters_list[rand_int]
            self.Your_password += random.choice(letters_list)

        for i in range(0, self.num_of_symbol):
            # rand_int = random.randint(0, len(gen.symbols_list)-1)
            # Your_password += gen.symbols_list[rand_int]
            self.Your_password += random.choice(symbols_list)

        for i in range(0, self.num_of_numbers):
            # rand_int = random.randint(0, len(gen.nums_list)-1)
            # Your_password += gen.nums_list[rand_int]
            self.Your_password += random.choice(nums_list)

        # Instead of assigning it this way we can also use
        # random.choice(gen.letters_list)

        # Final Password & Hard Level incorporated
        # So basically this does is, shuffle each and every element of string
        self.Your_password = "".join(random.sample(self.Your_password, len(self.Your_password)))
        # print(f"Generated Password: {self.Your_password}")
        return self.Your_password

# Well another way of incorporating Hard Level is that
# First we need to convert our Easy Level password to a list
# Then we can use random.shuffle(list)
# Finally again appending all the elements to a string = ""
