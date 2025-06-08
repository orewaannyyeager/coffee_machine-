Menu = {
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150
    },
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200
    }
}

profit = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredients):
    for item in order_ingredients:
        if item not in resources:
            print(f"Sorry, we don't have {item}.")
            return False
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    coins_five = int(input("How many 5 rupee coins? "))
    coins_ten = int(input("How many 10 rupee coins? "))
    coins_twenty = int(input("How many 20 rupee coins? "))
    total = (coins_five * 5) + (coins_ten * 10) + (coins_twenty * 20)
    return total


def is_payment_successful(money_received, coffee_cost):
    global profit
    if money_received >= coffee_cost:
        change = money_received - coffee_cost
        if change > 0:
            print(f"Here is Rs{change} in change.")
        profit += coffee_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False
def make_coffee(coffee_type):
    for item in coffee_type['ingredients']:
        resources[item] -= coffee_type['ingredients'][item]
    print(f"Here is your {coffee_type}. Enjoy! ☕")

is_on = True

while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffee = {resources['coffee']}g")
        print(f"Money = Rs{profit}")
    else:
        coffee_type = Menu.get(choice)
        if coffee_type:
            if check_resources(coffee_type['ingredients']):
                payment = process_coins()
                if is_payment_successful(payment, coffee_type['cost']):
                    make_coffee = input(f"Do you want to proceed with making {choice}? (yes/no): ")
                    if make_coffee.lower() == "yes":
                        for item in coffee_type['ingredients']:
                            resources[item] -= coffee_type['ingredients'][item]
                        print(f"Here is your {choice}. Enjoy! ☕")
                    else:
                        print("Order cancelled.")
        else:
            print("Invalid option. Please choose from espresso, latte, or cappuccino.")
