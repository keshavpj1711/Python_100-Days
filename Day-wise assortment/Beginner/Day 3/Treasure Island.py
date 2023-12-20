# Greetings
print("Welcome to Treasure Island"
      "Your Mission is to find the treasure")

# Working of the game
first_question = input("Which way do you wish to go left or right?")
if first_question == "left":
    second_question = input("Do you wish to wait for the boat or swim across the lake?")
    if second_question == "wait":
        third_question = input("There are three doors present red, blue and yellow, which door do you wish to choose?")
        if third_question == "red":
            print("The room was full of fire, Game Over")
        elif third_question == "yellow":
            print("You win")
        elif third_question == "blue":
            print("You are now a member of sharks, Game Over")
        else:
            print("Suicide, Game Over")
    else:
        print("You were a great meal to alligators, Game Over")
else:
    print("You fell into a hole, Game Over")