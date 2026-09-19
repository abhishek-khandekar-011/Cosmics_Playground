class CoffeeMaker:

    def __init__(self):
        self.resources = {"water": 300, "milk": 200, "coffee": 100}

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink["ingredients"]:
            if drink["ingredients"][item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order["ingredients"]:
            self.resources[item] -= order["ingredients"][item]
        print(f"Here is your {order['name']} ☕️. Enjoy!")


class MoneyMachine:

    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += (
                int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
            )
        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False


MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
        "name": "espresso",
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
        "name": "latte",
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
        "name": "cappuccino",
    },
}

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    options = "espresso/latte/cappuccino"
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in MENU:
        drink = MENU[choice]
        if coffee_maker.is_resource_sufficient(
            drink
        ) and money_machine.make_payment(drink["cost"]):
            coffee_maker.make_coffee(drink)
