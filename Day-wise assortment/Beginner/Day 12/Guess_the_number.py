# Importing required modules
import random
import sys


# defining function to check your choice
def check_answer(guess_no, answer_no):
    """
    Zero means too low,
    one means too high
    2 means correct answer
    """
    if guess_no < answer_no:
        return 0
    if guess_no > answer_no:
        return 1
    if guess_no == answer_no:
        return 2


# Generating a random number between 1 and 100
answer = random.randint(1, 100)
# Choosing difficulty
game_choice = input("Choose difficulty easy(e)/hard(h): ")
# Setting count to zero
count = 0
# About the game
if game_choice == 'e':
    print("You have 10 attempts to guess the number")
    count = 10
elif game_choice == 'h':
    print("You have 5 attempts to guess the number")
    count = 5

# Running the loop till we have attempts
while True:
    guess = int(input("Enter your guess: "))
    result = check_answer(guess, answer)
    count -= 1

    # Checking for answer
    if result == 0:
        print("Too Low!!")
    elif result == 1:
        print("Too High!!")
    else:
        print("Hurrah!! You guessed the number.")
        break

    print(f"{count} Attempts left")
    print("\n")

    # Checking if any attempts left
    if count == 0:
        print("Oops you have run out of attempts You Lose!!")
        break

sys.exit()