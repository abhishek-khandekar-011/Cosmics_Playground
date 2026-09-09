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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def resources_available(needed_ingredients):
    for item in needed_ingredients:
        if needed_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, not enough {item}.")
            return False
    return True

def deduct_resources(needed_ingredients):
    for item in needed_ingredients:
        resources[item] -= needed_ingredients[item]

def insert_coins():
    total = int(input("Enter the number of quarters: ")) * 0.25
    total += int(input("Enter the number of dimes: ")) * 0.10
    total += int(input("Enter the number of nickles: ")) * 0.05
    total += int(input("Enter the number of pennies: ")) * 0.01
    return total

def transaction_money(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        if choice in MENU:
            drink = MENU[choice]
            if resources_available(drink["ingredients"]):
                payment = insert_coins()
                if transaction_money(payment, drink["cost"]):
                    deduct_resources(drink["ingredients"])
                    print(f"Here is your {choice}. Enjoy!")
        else:
            print("Invalid selection.")
