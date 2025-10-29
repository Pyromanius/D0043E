def calculator():
    while True:
        try:
            n1 = input("Enter the first number: ")
            if n1.lower() == "exit":
                print("Goodbye!")
                break

            n1 = float(n1)

            n2 = input("Enter the second number: ")
            if n2.lower() == "exit":
                print("Goodbye!")
                break

            n2 = float(n2)

            operation = input("Choose an operation (+, -, *, /): ")
            if operation.lower() == "exit":
                print("Goodbye!")
                break

            if operation == "+":
                result = n1 + n2
            elif operation == "-":
                result = n1 - n2
            elif operation == "*":
                result = n1 * n2
            elif operation == "/":
                result = n1 / n2
            else:
                print("Invalid operation! Please choose +, -, *, or /.")
                continue

            print(f"Result: {result}")

        except ZeroDivisionError:
            print("Cannot divide by zero!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except Exception as excep:
            print(f"An unexpected error occurred: {excep}")
        finally:
            print("Calculation complete.\n")