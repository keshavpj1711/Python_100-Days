import re
# Info req to create a pwd generator
# Letters
# Symbols
# Numbers

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