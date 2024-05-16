# Importing the req modules
import random
import sys

# Our Blackjack rules
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

# Global variables to be used as flags for 'for' loop
count = 0
computer_count = 0
# Giving cards to both user and the computer
user_cards = []
computer_cards = []


# Defining the req functions
def sum_elements(a_list):
    final_sum = 0
    for i in a_list:
        final_sum += i

    return final_sum


def deal_card(card_list):
    return card_list[random.randint(0, len(card_list))-1]


def start_deal():
    global count
    global computer_count
    # Adding two cards initially
    for i in range(2):
        user_cards.append(deal_card(cards))
    # Showing both the cards initially
    print(f"Your cards: {user_cards}, current score: {sum_elements(user_cards)}")
    count += 1

    # Adding two cards initially
    for i in range(2):
        computer_cards.append(deal_card(cards))
    # Showing only the first card of the dealer until user hit stand or pass
    print(f"Computer's first card {computer_cards[0]}")
    computer_count += 1


def ace_change(user_list):
    if sum_elements(user_list) > 21:
        local_count = 0
        for i in user_list:
            if i == 11:
                break
            local_count += 1
        user_list[local_count] = 1
        return
    else:
        return


def play_blackjack():

    while True:
        # Starting the deal
        if count == 0 and computer_count == 0:
            # Calling the function to start the deal
            start_deal()

        # To choose whether to stand or hit
        choice = input("Type 'y' to get another card, type 'n' to pass: ")

        if choice == 'y':
            # After first time adding one card only
            user_cards.append(deal_card(cards))

            # If the drawn card is Ace and sum > 21 consider ace as 1 instead of 11
            ace_change(user_cards)

            # Showing all the available cards after adding
            print(f"Your cards: {user_cards}, final score: {sum_elements(user_cards)}")

        # Logic to show you lost if card sum > 21
        if sum_elements(user_cards) > 21:
            print("You Lose")
            sys.exit()

        # If computer gets a blackjack computer wins
        if sum_elements(computer_cards) == 21:
            if sum_elements(user_cards) == 21:
                print("Draw")
                break
            else:
                print(f"Computer cards: {computer_cards}, Computers score: {sum_elements(computer_cards)}")
                print("You Lose")

        elif choice == 'n':
            # Show Computer cards
            print(f"Computer cards: {computer_cards}, Computers score: {sum_elements(computer_cards)}")
            if sum_elements(computer_cards) < 17:
                while sum_elements(computer_cards) < 17:
                    print("Getting another card......")
                    computer_cards.append(deal_card(cards))
                    print(f"Computer cards: {computer_cards}, Computers score: {sum_elements(computer_cards)}")

            if sum_elements(computer_cards) > 21:
                print("You Win")
                break

            if sum_elements(computer_cards) < sum_elements(user_cards):
                print("You Win")
                sys.exit()

            if sum_elements(computer_cards) == sum_elements(user_cards):
                print("Draw")
                sys.exit()

            if sum_elements(computer_cards) > sum_elements(user_cards):
                print("You Lose")
                sys.exit()


# Greetings
while True:
    play_game = input("Do you wish to play a game of blackjack? Type 'y' for yes and 'n' for no: ")
    if play_game == 'y':
        play_blackjack()
    elif play_game == 'n':
        print("Exiting......")
        break
