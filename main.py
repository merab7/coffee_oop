from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def get_user_choice():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


def coffee_machine():
    coffee = Menu()
    cook = CoffeeMaker()
    money = MoneyMachine()

    while True:
        user_choice = get_user_choice()

        if user_choice == "off":
            print("\nCoffee machine is turned off.")
            break
        elif user_choice == "report":
            cook.report()
            money.report()
        elif user_choice in ["espresso", "latte", "cappuccino"]:
            items = MenuItem(name=coffee.find_drink(user_choice).name,
                             milk=coffee.find_drink(user_choice).ingredients["milk"],
                             water=coffee.find_drink(user_choice).ingredients["water"],
                             coffee=coffee.find_drink(user_choice).ingredients["coffee"],
                             cost=coffee.find_drink(user_choice).cost)
            print(f"Cost of your {user_choice} is: ${items.cost}")
            if cook.is_resource_sufficient(coffee.find_drink(user_choice)):
                if money.make_payment(items.cost):
                    cook.make_coffee(items)
                else:
                    continue
            else:
                continue
        else:
            print("\nWe do not have this kind of coffee. Please check your input.")


coffee_machine()
