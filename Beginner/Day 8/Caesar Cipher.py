# Importing req modules
import generator as gen
import art


# Defining all the important functions
def encrypt(message, shift_no):
    encrypted_msg = ""

    # Going through all the letters in message
    for i in message:
        # Finding index number of 'i'
        if i in gen.letters_list:
            index_no = gen.letters_list.index(i)
            index_of_encrypted_msg = (index_no + shift_no) % 26
            encrypted_msg += gen.letters_list[index_of_encrypted_msg]

        else:
            encrypted_msg += i

    print(f"Your encrypted message is {encrypted_msg}")


def decrypt(message, shift_no):
    decrypted_msg = ""

    # Going through all the letters in message
    for i in message:
        # Finding index number of 'i'
        if i in gen.letters_list:
            index_no = gen.letters_list.index(i)
            index_of_decrypted_msg = index_no - shift_no

            # This is to ensure we can decode any number of shift be it greater than 26
            while index_of_decrypted_msg < 0:
                index_of_decrypted_msg += 26

            # Adding to the decrypted_msg
            decrypted_msg += gen.letters_list[index_of_decrypted_msg]

        else:
            decrypted_msg += i

    print(f"Your decrypted message is {decrypted_msg}")


# Greetings
print(art.logo)

while True:
    # Taking input for encrypt or decrypt
    choice = input("Type 'e' to encrypt, 'd' to decrypt and 'exit' to exit out the program: ")

    # Checking the choice
    if choice == 'exit':
        print("Good Bye")
        break

    # Typing your message
    msg = input("Enter your message: ").lower()
    shift = int(input("Enter the shift number: "))

    # Applying all the conditions for choosing whether to encrypt or decrypt
    if choice == 'e':
        encrypt(msg, shift)

    elif choice == 'd':
        decrypt(msg, shift)

    else:
        print("Please choose among the given choices, Thank You")
        continue
