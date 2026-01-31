import random  # Imports Python's random module so we can generate random results

# This function creates and returns one row of slot machine symbols
def spin_row():
    # This list contains all possible symbols that can appear on the slot machine
    symbols = ['🍒', '🍉', '🍋', '🔔', '💫']

    # This line randomly selects 3 symbols from the list above
    # random.choice(symbols) picks ONE random symbol
    # range(3) means this happens 3 times
    # The result is stored in a list and returned
    # "_" is used because we don't need the loop variable itself
    return [random.choice(symbols) for _ in range(3)]

# This function prints the slot machine row in a clean and readable format
def print_row(row):
    # Prints a decorative top border
    print("*************************")

    # " | ".join(row) joins the symbols together with a separator
    # Example output: 🍒 | 🍋 | 🔔
    print(" | ".join(row))

    # Prints a decorative bottom border
    print("*************************")

# This function checks if the player won and calculates the payout
def get_payout(row, bet):
    # This checks if all three symbols in the row are exactly the same
    # Example: 🍒 🍒 🍒
    if row[0] == row[1] == row[2]:

        # If all symbols match, payout depends on the symbol
        # Each symbol has a different multiplier

        if row[0] == '🍒':
            return bet * 3  # Cherry gives 3x the bet

        elif row[0] == "🍉":
            return bet * 4  # Watermelon gives 4x the bet

        elif row[0] == "🍋":
            return bet * 5  # Lemon gives 5x the bet

        elif row[0] == "🔔":
            return bet * 10  # Bell gives 10x the bet

        elif row[0] == "💫":
            return bet * 10  # Star gives 10x the bet

    # If the symbols do not all match, the player wins nothing
    return 0
 
# This is the main function where the game runs
def main():
    balance = 100  # The player starts the game with $100

    # Prints the welcome message and game information
    print("*************************")
    print("Welcome to python Slots: ")
    print("Symbols: 🍒 🍉🍋 🔔 💫")
    print()
    print("*************************")

    # This loop keeps the game running as long as the player has money
    while balance > 0:
        # Shows the player how much money they currently have
        print(f"Current balance: ${balance}")

        # Asks the player how much they want to bet
        bet = input("Place your bet amount: ")
        print()

        # Checks if the input contains only numbers
        # If not, the loop restarts
        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        # Converts the bet from a string to an integer
        bet = int(bet)

        # Checks if the player is betting more than they have
        if bet > balance:
            print("Insuficient funds")
            continue

        # Ensures the bet is greater than zero
        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        # Subtracts the bet amount from the balance before spinning
        balance -= bet

        # Spins the slot machine by generating random symbols
        row = spin_row()
        print("Spinning...\n")

        # Displays the slot result
        print_row(row)

        # Calculates how much the player won (if anything)
        payout = get_payout(row, bet)

        # Checks if the player won money
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry you lost this round")

        # Adds the winnings back to the player's balance
        balance += payout

        # Asks the player if they want to keep playing
        play_again = input("Do you want to spin again? (Y/N): ").upper()

        # If the player does not enter 'Y', the game stops
        if play_again != 'Y':
            break

    # This message is shown after the game loop ends
    # It runs when the player quits or runs out of money
    print("*******************************************")
    print(f"Game over your final balance is ${balance}")
    print("*******************************************")

# This ensures the program only runs when this file is executed directly
# It prevents the game from running if the file is imported into another program
if __name__ == '__main__':
    main()
