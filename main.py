from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_true = True

while is_true:

    menu = Menu()
    options = menu.get_items()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    choice = input(f"What would you like? ({options}): ")

    if choice == "report":

        coffee_maker.report()
        money_machine.report()

    elif choice == "off":

        break

    else:

        drink = menu.find_drink(choice)
        is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)

        if is_resource_sufficient:
            payment = money_machine.make_payment(drink.cost)

            if payment:
                coffee_maker.make_coffee(drink)






