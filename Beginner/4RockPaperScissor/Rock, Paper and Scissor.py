# Importing all req module
import random
import sys

# Input arts
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
available_choices = [rock, paper, scissors]

# Greetings and taking input
choice = int(input("What do you choose? \n0 for rock\n1 for paper\n2 for scissors\nChoose : "))
if choice < 0 or choice > 2:
    print("You typed a wrong number, You Lose!")
    sys.exit()

print(available_choices[choice])

# Generating random inputs
random_choice = random.randint(0, 2)
print("Computer Chose : ")
print(available_choices[random_choice])

# Final Logic
if choice == random_choice:
    print("It's a draw")

elif choice == 0:
    if random_choice == 1:
        print("You Lose")

    elif random_choice == 2:
        print("You Win")

elif choice == 1:
    if random_choice == 0:
        print("You Win")
    elif random_choice == 2:
        print("You Lose")

elif choice == 2:
    if random_choice == 0:
        print("You Lose")
    elif random_choice == 1:
        print("You Win")
