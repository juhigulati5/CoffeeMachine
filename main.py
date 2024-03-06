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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}


def sufficient_resources(user_input):
    """Returns true when order can be made, false when ingredients are insufficient."""
    ingredients = MENU[user_input]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
        else:
            return True


def enough_coins(user_input):
    """Calculates total of coins user inserted, returns true when enough money has been put in,
     false when funds are insufficient."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    user_amount = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)

    coffee_cost = MENU[user_input]["cost"]
    global profit

    if user_amount < coffee_cost:
        print("Sorry, that's not enough. Money refunded.")
        return False
    elif user_amount > coffee_cost:
        change = user_amount - coffee_cost
        rounded_change = round(change, 2)
        print(f"Here is ${rounded_change} in change.")
        profit += coffee_cost
        return True
    elif user_amount == coffee_cost:
        profit += coffee_cost
        return True


def update_resources(user_input):
    ingredients = MENU[user_input]["ingredients"]
    for item in ingredients:
        new_resource_total = resources[item] - ingredients[item]
        resources[item] = new_resource_total


def make_coffee(user_input):
    print(f"Here is your {user_input}☕. Enjoy!")


keep_going = True


while keep_going:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_type == "cappuccino" or coffee_type == "latte" or coffee_type == "espresso":
        if sufficient_resources(coffee_type):
            if enough_coins(coffee_type):
                update_resources(coffee_type)
                make_coffee(coffee_type)
    if coffee_type == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")

    elif coffee_type == "off":
        keep_going = False

