MENU = {
    "espresso":
        {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
    "latte":
        {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
    "cappuccino":
        {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def report(money):
    for i in resources:
        print(f"{i.title()}: {resources[i]}ml")
    print(f"Money: ${money}")


def coins():
    """Returns total sum of the money"""
    print("Please Insert Coins:")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def make_coffe_resources(resources):
    for i in MENU[desire]["ingredients"]:
        resources[i] -= MENU[desire]["ingredients"][i]


def sufficient():
    for i in MENU[desire]["ingredients"]:
        if resources[i] < MENU[desire]["ingredients"][i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True

profit = 0
while True:
    desire = input("What would you like? (espresso/latte/cappuccino):").lower()
    if desire == "off":
        print("Goodbye")
        break
    if desire == "report":
        report(profit)
    elif sufficient():
        drink_cost = MENU[desire]["cost"]
        resto = coins() - drink_cost

        if resto > 0:
            make_coffe_resources(resources)
            profit += drink_cost
            print(f"Here is ${round(resto, 2)} in change.")
            print(f"Here is your {desire} ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")

# TODO 1. Print resources with report
# TODO 2. Check resources sufficient
