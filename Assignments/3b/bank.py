def deposit(balance):
    amount = int(input("Enter the amount to deposit: "))
    balance += amount
    print(f"You have successfully deposited ${amount}. Your new balance is: ${balance}")


def withdraw(balance):
        amount = int(input("Enter the amount to withdraw: $"))
        if amount > balance:
            print(f"Insufficient balance! You only have ${balance} in your account.")
        else:
            balance -= amount
            print(f"You have successfully withdrawn ${amount}. Your new balance is: ${balance}")


balance = 1000

print("Welcome To Simple bank!\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
choice = int(input("Choose an option (1-4): "))

if choice == 1:
    print(f"Your current balance is: ${balance}")
elif choice == 2:
    deposit(balance)
elif choice == 3:
    withdraw(balance)
elif choice == 4:
    print("Thank you for using Simple Bank! Goodbye!")
else:
    print("Invalid choice! Please select a valid option (1-4).")