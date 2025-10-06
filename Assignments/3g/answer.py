def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    result = b
    for i in range(1, a):
        result = result + b
    return result


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Which operation would you like to perform? (+, -, *, /): ")

if operation not in ['+', '-', '*', '/']:
    print("Invalid operation")
else:
    if operation == '+':
        print(f"The result of {a} + {b} is {add(a, b)}")
    elif operation == '-':
        print(f"The result of {a} - {b} is {subtract(a, b)}")
    elif operation == '*':
        print(f"The result of {a} * {b} is {multiply(a, b)}")
    elif operation == '/':
        print(f"The result of {a} / {b} is {divide(a, b)}")
