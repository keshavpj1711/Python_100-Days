# Getting the req modules
import os


# Defining the necessary function
def clear_console():
    os.system('cls')


# Greetings
print("Welcome to Silent Auction")

# Declaring your main dictionary
bid_dict = {}

# First Bid
first_name = input("Enter your name: ")
first_bid = float(input("Enter your bid: Rs"))
bid_dict[first_name] = first_bid

# Highest Bidder and Bid
highest_bidder = ""
highest_bid = 0

while True:
    continue_choice = input("If you want to add another bid type 'y', or type 'n' to display the bid results: ").lower()
    if continue_choice == 'y':
        clear_console()
        name = input("Enter your name: ")
        bid = float(input("Enter your bid: Rs"))
        bid_dict[name] = bid

    elif continue_choice == 'n':
        for i in bid_dict:
            if bid_dict[i] > highest_bid:
                highest_bid = bid_dict[i]
                highest_bidder = i

        break

    else:
        print("Please choose something from the choices provided, THANK YOU")
        continue

print("\n")
print(f"The shown artifact is sold to {highest_bidder} for {highest_bid} Rs")

input("Press any button to exit the program")