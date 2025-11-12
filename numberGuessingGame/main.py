# Import the random module to generate random numbers
import random

# Game settings - change these to adjust the difficulty
lowest_num = 1      # The smallest number you can guess
highest_num = 100   # The largest number you can guess
answer = random.randint(lowest_num, highest_num)  # Computer picks a random secret number
guesses = 0         # Counter to track how many guesses the player makes

# Game control variable - keeps the game running until player wins
is_running = True

# Display game title and instructions
print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

# Main game loop - keeps running until player guesses correctly
while is_running:
    # Get the player's guess
    guess = input("Enter your guess: ")
    
    # Check if the input is a valid number (digits only)
    if guess.isdigit():
        # Convert the input from text to an integer number
        guess = int(guess)
        guesses += 1  # Increase guess count by 1
        
        # Check if guess is outside the allowed range
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")
        
        # Check if guess is too low
        elif guess < answer:
            print("Too low! try again!")
        
        # Check if guess is too high  
        elif guess > answer:
            print("Too high! try again!")
        
        # If none of the above, guess must be correct!
        else:
            print(f"CORRECT! The number was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False  # This ends the game loop
    
    # If input is not a valid number (contains letters or symbols)
    else:
        print("Invalid guess")
        print(f"Please enter a number between {lowest_num} and {highest_num}")

# Game ends here - the loop stops when is_running becomes False