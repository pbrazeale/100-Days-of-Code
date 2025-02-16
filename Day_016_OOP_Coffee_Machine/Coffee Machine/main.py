from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def requesting():
    global menu
    request = input(f"What would you like? {menu.get_items()}:  ").lower()
    
    if request == "report":
        coffee_maker.report()
        money_machine.report()
        requesting()
    elif request == "off":
        sys.exit()
    else:
        return menu.find_drink(request)
    

def main():
    global coffee_maker, money_machine
    drink = requesting()

    if coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

 
if __name__ == "__main__":
    main()