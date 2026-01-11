import random  # Import the random module to generate random numbers

# Define the lowest and highest numbers the user can guess
lowest_num = 1
highest_num = 100

# Generate a random number between lowest_num and highest_num
answer = random.randint(lowest_num, highest_num)

# Variable to count how many guesses the user makes
guesses = 0

# This variable controls whether the game keeps running
is_running = True

# Display the game title
print("Python Number Guessing Game")

# Tell the user the valid number range
print(f"Select a number between {lowest_num} and {highest_num}")

# Loop that runs until the correct number is guessed
while is_running:

    # Ask the user to enter a guess (input is always a string)
    guess = input("Enter your guess: ")

    # Check if the input contains only digits (prevents crashes)
    if guess.isdigit():

        # Convert the string input into an integer
        guess = int(guess)

        # Increase the number of guesses by 1
        guesses += 1

        # Check if the guess is outside the allowed range
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Select a number between {lowest_num} and {highest_num}")

        # Check if the guess is too low
        elif guess < answer:
            print("Too low! Try again.")

        # Check if the guess is too high
        elif guess > answer:
            print("Too high! Try again.")

        # If none of the above are true, the guess is correct
        else:
            print(f"🎉 CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")

            # Stop the game loop
            is_running = False

    # Runs if the input is not a number
    else:
        print("Invalid guess")
        print(f"Select a number between {lowest_num} and {highest_num}")
4
