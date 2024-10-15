# Import statements (adjusted for non-Replit environments)
# from replit import clear  # Uncomment if running in Replit
from art import logo

def add(n1, n2):
    """Return the sum of n1 and n2."""
    return n1 + n2

def subtract(n1, n2):
    """Return the difference between n1 and n2."""
    return n1 - n2

def multiply(n1, n2):
    """Return the product of n1 and n2."""
    return n1 * n2

def divide(n1, n2):
    """Return the division of n1 by n2."""
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}



def calculator():
    """Perform calculations based on user input."""
    print(logo)
    num1 = float(input("What's the first number?: "))
    
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        
        if operation_symbol not in operations:
            print("Invalid operation. Please choose a valid operation.")
            continue
        
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        next_step = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ").lower()
        
        if next_step == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator() #recursion function calling itself inside its own fnction definition.

calculator()
