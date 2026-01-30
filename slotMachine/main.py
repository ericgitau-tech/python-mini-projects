import random  # Imports the random module to generate random choices

# This function generates one row of slot symbols
def spin_row():
    # List of possible slot symbols
    symbols = ['🍒', '🍉', '🍋', '🔔', '💫']

    # Uses list comprehension to randomly select 3 symbols
    # "_" is used because the loop variable itself is not needed
    return [random.choice(symbols) for _ in range(3)]

# This function prints the slot row in a formatted way
def print_row(row):
    print("*************************")
    # Joins the symbols in the row with " | " between them
    print(" | ".join(row))
    print("*************************")

# This function calculates how much the user wins
def get_payout(row, bet):
    # Checks if all three symbols in the row are the same
    if row[0] == row[1] == row[2]:
        # Determines payout multiplier based on the symbol
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "💫":
            return bet * 10
    # Returns 0 if there is no winning combination
    return 0
 
# Main function that runs the slot machine game
def main():
    balance = 100  # Starting balance for the player

    # Displays welcome message and game info
    print("*************************")
    print("Welcome to python Slots: ")
    print("Symbols: 🍒 🍉🍋 🔔 💫")
    print()
    print("*************************")

    # Game loop continues while the player has money
    while balance > 0:
        print(f"Current balance: ${balance}")

        # Takes bet input from the user
        bet = input("Place your bet amount: ")
        print()

        # Validates that the bet is a number
        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        # Checks if the bet exceeds available balance
        if bet > balance:
            print("Insuficient funds")
            continue

        # Ensures the bet is greater than zero
        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        # Deducts the bet from the balance
        balance -= bet

        # Spins the slot machine
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        # Calculates payout
        payout = get_payout(row, bet)

        # Displays result of the spin
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        # Adds winnings back to the balance
        balance += payout

        # Asks player if they want to continue playing
        play_again = input("Do you want to spin again? (Y/N): ").upper()

        # Ends the game if the player chooses not to continue
        if play_again != 'Y':
            break

# Ensures the program runs only when executed directly
if __name__ == '__main__':
    main()
