from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

print("------ REPORT------")
print(coffee_maker.report(), "\n" * 2)


for item in menu.menu:
    print(f"{item.name} costs ${item.cost}")

drink_name = input("Select your drink: 'latte' / 'espresso' / 'cappuccino': ").lower()

drink = menu.find_drink(drink_name)

check_resources = coffee_maker.is_resource_sufficient(drink)

process_coin = money_machine.make_payment(drink.cost)

make_coffee = coffee_maker.make_coffee(drink)

print("------ REPORT------")
print(coffee_maker.report(), "\n" * 2)