# Import the random module
# This allows the computer to make a random choice
import random

# A tuple that stores all possible game options
# Tuple is used because these values should not change
options = ("rock", "paper", "scissors")

# Variable to store the player's choice
# None means "no value yet"
player = None

# Boolean variable to keep the game running
running = True

# Main game loop
# The game will keep running as long as running is True
while running:

    # Reset player choice at the start of each round
    player = None

    # Keep asking the player until a valid option is entered
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    # Computer randomly chooses one option from the tuple
    computer = random.choice(options)

    # Display both choices
    print(f"\nPlayer: {player}")
    print(f"Computer: {computer}")

    # Check for a tie
    if player == computer:
        print("It's a tie!")

    # Winning conditions for the player
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")

    # If none of the winning conditions match, the player loses
    else:
        print("You lose!")

    # Ask the player if they want to play again
    play_again = input("\nPlay again? (y / n): ").lower()

    # If the player does NOT enter "y", stop the game
    if play_again != "y":
        running = False

# This line runs after the loop ends
print("\nThanks for playing!")
