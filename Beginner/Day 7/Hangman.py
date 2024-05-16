# Importing necessary modules
import random, Hangman_art, Hangman_wordlist


# Defining a function to print the list in clean format
def list_print(test_list):
    for item in test_list:
        print(item, end=" ")
    print("\n")


# Greetings
print(Hangman_art.logo)

# Choosing our word from the given word list
chosen_word = Hangman_wordlist.word_list[random.randint(0, len(Hangman_wordlist.word_list) - 1)]

# Creating a list to display the output
display = []
for i in chosen_word:
    display += "_"

# Deciding the number of lives we want to give our user
lives = 6

# Final Logic of the program
while lives > 0:
    guess = input("Guess a letter: ").lower()

    # To check and replace the blanks with correct letter in display list
    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    # Checking if the word is completed or not
    if "".join(display) == chosen_word:
        list_print(display)
        print("You Win")
        break

    # Displaying the list after every input
    list_print(display)

    # Checking if the guess is present in the chosen word or not
    # If not then reducing the life by one
    if guess not in chosen_word:
        lives -= 1
    print(Hangman_art.stages[lives])

    # Finally if the lives turn to zero the user loses the game and we break out of loops
    if lives == 0:
        print("You Lose")
        print("Game Over")
        print(f"The Correct Word is {chosen_word}")
        break
