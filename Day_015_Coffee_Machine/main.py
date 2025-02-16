import sys

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# GLOBAL
request = ""

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")
    customer_request()

def process_change(quarters, dimes, nickles, pennies):
    global request
    q = quarters * 0.25
    d = dimes * 0.1
    n = nickles * 0.05
    p = pennies * 0.01
    coins = q+d+n+p
    drink_cost = MENU[request]["cost"]

    if drink_cost > coins:
        print(f"Sorry that's not enough money. Drink costs ${drink_cost:.2f} Money refunded ${coins:.2f}")
        return main()
    elif (coins - drink_cost) > resources["money"]:
        print(f"Insufecent change in machine. Money refunded ${coins:.2f}")
    else:
        change = coins - drink_cost
        if change == 0:
            resources["money"] += coins
        else:
            print(f"Here is ${change:.2f} dollars in change.”")
            resources["money"] += coins
            resources["money"] -= change

def insert_coins():
    global request
    print("Please insert coins.")
    quarters = int(input("How many quarters?:  "))
    dimes = int(input("How many dimes?:  "))
    nickles = int(input("How many nickles?:  "))
    pennies = int(input("How many pennies?:  "))
    process_change(quarters, dimes, nickles, pennies)

def insufecent_resources(item):
    print(f"Sorry there is not enough {item}")
    main()

def resource_check():
    global request
    water = MENU[request]["ingredients"]["water"]
    coffee = MENU[request]["ingredients"]["coffee"]
    
    try:
        milk = MENU[request]["ingredients"]["milk"]
    except:
        milk = 0
    
    if water > resources["water"]:
        insufecent_resources("water")
    elif milk > resources["milk"]:
        insufecent_resources("milk")
    elif coffee > resources["coffee"]:
        insufecent_resources("coffee")
    else:
        return

def pour_coffee():
    global request
    resources["water"] = resources["water"] - MENU[request]["ingredients"]["water"]
    try:
        resources["milk"] = resources["milk"] - MENU[request]["ingredients"]["milk"]
    except:
        pass
    resources["coffee"] = resources["coffee"] - MENU[request]["ingredients"]["coffee"]
    print(f"Here is your {request}. Enjoy!")


def make_drink():
    global request
    resource_check()
    insert_coins()
    pour_coffee()
    main()

def customer_request():
    global request
    request = input(f"What would you like? ('espresso' ${MENU["espresso"]["cost"]:.2f}/'latte' ${MENU["latte"]["cost"]:.2f}/'cappuccino' ${MENU["cappuccino"]["cost"]:.2f}):  ").lower()
    if request == "report":
        report()
    elif request == "espresso" or request == "latte" or request == "cappuccino":
        return
    elif request == "off":
        sys.exit()
    else:
        print("Not a recognized request")
        customer_request()

def main():
    customer_request()
    make_drink()


main()