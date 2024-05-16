# Import required modules
import os
import random
import art
import game_data as gd  # Length of database is 50
# import sys


# Define a function to generate random number
def random_no():
    return random.randint(0, 49)


def check_higher(person1, person2):
    if person1["follower_count"] >= person2["follower_count"]:
        return "A"
    else:
        return "B"


# Setting value of A and B and count
A = gd.data[random_no()]
B = gd.data[random_no()]
count = 0

while True:
    print(art.logo)
    print(f"Current Score: {count}")
    print(f"A: {A["name"]}, a {A["description"]}, from {A["country"]}")
    print(art.vs)
    print(f"B: {B["name"]}, a {B["description"]}, from {B["country"]}")
    choice = input("Who has more followers A or B? Type 'A' or 'B': ")
    choice = choice.upper()

    # If A has more or equal followers than answer = "A"
    # If B has more or followers than answer = "B"
    answer = check_higher(A, B)

    # Now checking for correct answer
    if choice == answer:
        A = B
        B = gd.data[random_no()]
        count += 1
    else:
        print("")
        print("Sorry!! You Lose")
        print(f"Your score: {count}")
        break
    # sys.stdout.flush()
    os.system('cls' if os.name == 'nt' else 'clear')
