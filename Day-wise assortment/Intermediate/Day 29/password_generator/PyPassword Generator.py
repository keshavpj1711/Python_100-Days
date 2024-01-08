# Importing req modules
import random
import generator as gen


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
            self.Your_password += random.choice(gen.letters_list)

        for i in range(0, self.num_of_symbol):
            # rand_int = random.randint(0, len(gen.symbols_list)-1)
            # Your_password += gen.symbols_list[rand_int]
            self.Your_password += random.choice(gen.symbols_list)

        for i in range(0, self.num_of_numbers):
            # rand_int = random.randint(0, len(gen.nums_list)-1)
            # Your_password += gen.nums_list[rand_int]
            self.Your_password += random.choice(gen.nums_list)

        # Instead of assigning it this way we can also use
        # random.choice(gen.letters_list)

        # Final Password & Hard Level incorporated
        # So basically this does is, shuffle each and every element of string
        self.Your_password = "".join(random.sample(self.Your_password, len(self.Your_password)))
        # print(f"Generated Password: {self.Your_password}")

# Well other way of incorporating Hard Level is that
# First we need to convert our Easy Level password to a list
# Then we can use random.shuffle(list)
# Finally again appending all the elements to a string = ""
