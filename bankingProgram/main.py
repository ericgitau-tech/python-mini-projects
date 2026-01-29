# Function to display the current account balance
def show_balance(balance):
    # Print decorative line
    print("***************************")

    # Display the balance formatted to 2 decimal places
    print(f"Your balance is ${balance:.2f}")

    # Print decorative line
    print("***************************")


# Function to handle depositing money
def deposit():
    # Ask the user to enter the deposit amount and convert it to float
    amount = float(input("Enter the amount to be deposited: "))

    # Print decorative line
    print("***************************")

    # Check if the amount entered is negative
    if amount < 0:
        # If invalid amount, show error message
        print("That's not a valid amount")

        # Return 0 so balance does not change
        return 0
    else:
        # Return the valid deposit amount
        return amount


# Function to handle withdrawing money
def withdraw(balance):
    # Print decorative line
    print("***************************")

    # Ask the user to enter the withdrawal amount
    amount = float(input("Enter amount to be withdrawn: "))

    # Check if withdrawal amount is greater than current balance
    if amount > balance:
        # If not enough money, show error message
        print("Insufficient funds")

        # Return 0 so balance does not change
        return 0

    # Check if withdrawal amount is negative
    elif amount < 0:
        # Show error message for invalid amount
        print("Amount must be greater than 0")

        # Return 0 so balance does not change
        return 0

    else:
        # Return the valid withdrawal amount
        return amount


# Main function that controls the program
def main():
    # Initialize account balance to 0
    balance = 0

    # Boolean variable to keep the program running
    is_running = True

    # Loop that keeps showing the menu until user exits
    while is_running:
        # Display the menu
        print("*****************************")
        print("        Banking Program      ")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*****************************")

        # Ask user to choose an option
        choice = input("Enter your choice (1-4): ")

        # Option 1: Show balance
        if choice == '1':
            show_balance(balance)

        # Option 2: Deposit money
        elif choice == '2':
            balance += deposit()

        # Option 3: Withdraw money
        elif choice == '3':
            balance -= withdraw(balance)

        # Option 4: Exit the program
        elif choice == '4':
            is_running = False

        # Handle invalid menu choices
        else:
            print("***************************")
            print("That is not a valid choice.")
            print("***************************")

    # Message displayed after exiting the program
    print("***************************")
    print("Thank you! Have a nice day!")
    print("***************************")


# Program entry point
# This ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
