# Importing req modules
import random
import generator as gen

# Greetings for our program
print("Welcome to PyPassword Generator")
num_of_letters = random.randint(8, 10)
num_of_symbol = random.randint(2, 4)
num_of_numbers = random.randint(2, 4)

total_len = num_of_symbol + num_of_numbers + num_of_letters

# Doing the easy level
# letterssymbolnumbers

# Easy Level
Your_password = ""
for i in range(0, num_of_letters):
    # rand_int = random.randint(0, len(gen.letters_list)-1)
    # Your_password += gen.letters_list[rand_int]
    Your_password += random.choice(gen.letters_list)

for i in range(0, num_of_symbol):
    # rand_int = random.randint(0, len(gen.symbols_list)-1)
    # Your_password += gen.symbols_list[rand_int]
    Your_password += random.choice(gen.symbols_list)


for i in range(0, num_of_numbers):
    # rand_int = random.randint(0, len(gen.nums_list)-1)
    # Your_password += gen.nums_list[rand_int]
    Your_password += random.choice(gen.nums_list)

# Instead of assigning it this way we can also use
# random.choice(gen.letters_list)

# Final Password & Hard Level incorporated
Your_password = "".join(random.sample(Your_password, len(Your_password)))
print(f"Generated Password: {Your_password}")

# Well other way of incorporating Hard Level is that
# First we need to convert our Easy Level password to a list
# Then we can use random.shuffle(list)
# Finally again appending all the elements to a string = ""
