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

machine_on = True
profit = 0


def check_resources(ingredients):
    """Checks if there are enough resources to make the selected drink."""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there's not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total $ amount from the users inserted coins."""
    print(f"Please insert: ${price}0 in coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def process_transaction(users_payment, coffee_price):
    """Checks if user's payment will cover the cost of coffee price."""
    if users_payment >= coffee_price:
        change = round(users_payment - coffee_price, 2)
        if change > 0:
            print(f"Your change is ${change}.")
        else:
            print("Your purchase has been successfully processed.")
        global profit
        profit += coffee_price
        return True
    else:
        print("Not enough funds were inserted, money has been refunded.")
        return False


def make_coffee(coffee, ingredients):
    """Deduct the ingredients used from ingredients in machine."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    return print(f"Your {coffee} is ready! ☕️.")


while machine_on:
    user_choice = input("What would you like?: Espresso, Latte, or Cappuccino.\n").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources["water"]}mL")
        print(f"Milk: {resources["milk"]}mL")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Bank: ${profit}")
    else:
        drink = MENU[user_choice]
        price = MENU[user_choice]["cost"]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if process_transaction(payment, drink["cost"]):
                make_coffee(user_choice.capitalize(), drink["ingredients"])