def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

def calculator():

    continue_with_calculation = True
    first_number = float(input("Enter first number?: "))

    while continue_with_calculation:
        for symbol in operations:
            print(symbol)

        symbol = input("Enter operartions?: ")
        second_number = float(input("Enter second number?: "))

        result = operations[symbol](first_number, second_number)
        
        print(f"{first_number} {symbol} {second_number} = {result}")
        
        continue_calculation = input("Do want to continue with the calculation? Type 'Yes' to continue or 'No' to cancel: ").lower()
        
        if continue_calculation == 'yes':
            first_number = result
        else:
            continue_calculation = False
            print("New Calculation starts!")
            print("\n" * 30)
            calculator()

calculator()