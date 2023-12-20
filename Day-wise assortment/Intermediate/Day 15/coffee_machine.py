# Few instructions
# 1. art.py should be as same dir as that of coffee_machine.py
# 2. The inputs that choice can take are
#     a. e, l and c for getting you the requested coffee
#     b. off to turn on the coffee machine and,
#     c. Report to get the report about milk, water, coffee and the money_collected

# importing coffee art
import art

# Required Dictionaries menu and resources
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 150,
    "money_collected": 0,
}


# Defining functions to make different coffees
def make_espresso():
    # Checking for sufficient resources
    # Returning 0 if coffee is not made
    # Returning 1 if coffee is made
    if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
        print("Sorry insufficient water.")
        return 0
    elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
        print("Sorry insufficient coffee.")
        return 0
    else:
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        return 1


def make_latte():
    # Checking for sufficient resources
    # Returning 0 if coffee is not made
    # Returning 1 if coffee is made
    if resources["water"] < MENU["latte"]["ingredients"]["water"]:
        print("Sorry insufficient water.")
        return 0
    elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
        print("Sorry insufficient coffee.")
        return 0
    elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
        print("Sorry insufficient milk.")
        return 0
    else:
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        return 1


def make_cappuccino():
    # Checking for sufficient resources
    # Returning 0 if coffee is not made
    # Returning 1 if coffee is made
    if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
        print("Sorry insufficient water.")
        return 0
    elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
        print("Sorry insufficient coffee.")
        return 0
    elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
        print("Sorry insufficient milk.")
        return 0
    else:
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        return 1


# Processing Coins
def process_coins(coffee_type):
    penny = int(input("Enter the number of pennies: "))
    penny *= 0.01
    nickel = int(input("Enter the number of nickles: "))
    nickel *= 0.05
    dime = int(input("Enter the number of dimes: "))
    dime *= 0.1
    quarter = int(input("Enter the number of quarters: "))
    quarter *= 0.25
    total_coins = penny+nickel+dime+quarter
    print(f"Inserted amount: ${total_coins}")
    if coffee_type == 'e':
        change = total_coins - MENU["espresso"]["cost"]
        if total_coins >= MENU["espresso"]["cost"]:
            # if coffee is not made, don't deduct coins
            if make_espresso() == 0:
                return
            else:
                # Making changes to the money collected
                resources["money_collected"] += MENU["espresso"]["cost"]
                print("Don't forget to take your coffee...")
                print(art.coffee)
                print(f"Here's your change: ${change}")
                return
        else:
            print("Insufficient coins")
            print("Returning coins....")
            return

    elif coffee_type == 'l':
        change = total_coins - MENU["latte"]["cost"]
        if total_coins >= MENU["latte"]["cost"]:
            # if coffee is not made, don't deduct coins
            if make_latte() == 0:
                return
            else:
                # Making changes to the money collected
                resources["money_collected"] += MENU["latte"]["cost"]
                print("Don't forget to take your coffee...")
                print(art.coffee)
                print(f"Here's your change: ${change}")
                return
        else:
            print("Insufficient coins")
            print("Returning coins....")
            return

    elif coffee_type == 'c':
        change = total_coins - MENU["cappuccino"]["cost"]
        if total_coins >= MENU["cappuccino"]["cost"]:
            # if coffee is not made, don't deduct coins
            if make_cappuccino() == 0:
                return
            else:
                # Making changes to the money collected
                resources["money_collected"] += MENU["cappuccino"]["cost"]
                print("Don't forget to take your coffee...")
                print(art.coffee)
                print(f"Here's your change: ${change}")
                return
        else:
            print("Insufficient coins")
            print("Returning coins....")
            return


# Greetings
print(art.greetings)

while True:
    # Prompt user what would he like
    print('')
    choice = input("What would you like?(espresso(e)/latte(l)/cappuccino(c)): ")

    # Conditional statements for choice
    if choice == 'off':
        break
    elif choice == 'report':
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money_collected"]}")
    elif choice == 'e':
        process_coins('e')
    elif choice == 'l':
        process_coins('l')
    elif choice == 'c':
        process_coins('c')
