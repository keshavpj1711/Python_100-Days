from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating the required objects
coffee1 = MenuItem("espresso", 100, 0, 18, 1.5)
coffee2 = MenuItem("latte", 200, 150, 24, 2.5)
coffee3 = MenuItem("cappuccino", 250, 100, 24, 3)
menu_list = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while True:
    choice = input(f"What do you choose? {menu_list.get_items()}: ")
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        break
    else:
        drink = menu_list.find_drink(choice)
        drink_possible = coffee_maker.is_resource_sufficient(drink)
        if drink_possible:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
