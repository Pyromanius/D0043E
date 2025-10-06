def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    result = b
    for i in range (0, a):
        result = result + b
    return result

def divide(a, b):   
    if b == 0:
        return "Error: Division by zero"
    return a / b

def get_numbers():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

operation = input("Which operation would you like to perform? (+, -, *, /): ")

if not operation in ['+', '-', '*', '/']:
    print("Invalid operation")
else:
    print("The result is: ")
    if operation == '+':
        get_numbers
    elif operation == '-':
        get_numbers
    elif operation == '*':
        get_numbers
    elif operation == '/':
        get_numbers

