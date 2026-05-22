# Virtual Cofffe machine
from menu import resources, MENU

is_on = True
profit = 0;

# Check if resource is sufficient to prepare drink
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] <= resources[item]:
            return True
        else:
            print(f"Sorry there is not enough {item}.")
            return False

def check_transaction(cost, total):
    change = 0
    is_transaction_successfull = False
    if total < cost:
        print("Sorry that's not enough money. Money refunded")
    elif total == cost:
        profit += total
        is_transaction_successfull = True
    elif total > cost:
        change = total - cost
        print(f"Here is ${change} dollars in change.")
        is_transaction_successfull = True
    
    return [change, is_transaction_successfull]


# Proccess coins: quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def process_coins():
    print("Please insert coins. 'quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01'")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return round(total, 2)
    


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)

        if is_resource_sufficient(drink['ingredients']):
            total_coins = process_coins()
            transaction_state = check_transaction(drink['cost'], total_coins)

            if transaction_state[1]:
                resources['water'] -= drink['ingredients']['water']
                # resources['milk'] -= drink['ingredients']['milk']
                resources['milk'] -= drink['ingredients'].get('milk', 0)
                resources['coffee'] -= drink['ingredients']['coffee']
                profit += drink['cost']
                print(f"Here is your {choice}. Enjoy!")