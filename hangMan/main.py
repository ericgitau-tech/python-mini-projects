# Import the random module
# This module allows us to randomly select a word from the word list
import random

# Import the list of words from an external file named wordlist.py
# The file should contain a variable called `words`, which is a list of strings
# Example:
# words = ["python", "hangman", "programming"]
from wordlist import words


# -----------------------------------
# HANGMAN ASCII ART REPRESENTATION
# -----------------------------------
# This dictionary maps the number of wrong guesses to
# the corresponding Hangman drawing.
#
# Each value is a tuple of strings.
# Each string represents one line of the Hangman figure.
#
# As the number of wrong guesses increases, the drawing
# becomes more complete.
hangman_art = {
    0: (
        "   ",
        "   ",
        "   "
    ),
    1: (
        " o ",
        "   ",
        "   "
    ),
    2: (
        " o ",
        " | ",
        "   "
    ),
    3: (
        " o ",
        "/| ",
        "   "
    ),
    4: (
        " o ",
        "/|\\",
        "   "
    ),
    5: (
        " o ",
        "/|\\",
        "/  "
    ),
    6: (
        " o ",
        "/|\\",
        "/ \\"
    )
}


# -----------------------------------
# FUNCTION: DISPLAY HANGMAN DRAWING
# -----------------------------------
def display_man(wrong_guesses):
    # Print a decorative separator
    print("\n**************************")

    # Loop through each line of the Hangman drawing
    # corresponding to the current number of wrong guesses
    for line in hangman_art[wrong_guesses]:
        print(line)

    # Print another separator
    print("**************************")


# -----------------------------------
# FUNCTION: DISPLAY CURRENT WORD HINT
# -----------------------------------
def display_hint(hint):
    # Display the word hint with spaces between characters
    # Example: _ _ a _ _
    print("Word:", " ".join(hint))


# -----------------------------------
# FUNCTION: DISPLAY FINAL ANSWER
# -----------------------------------
def display_answer(answer):
    # Display the correct word after the game ends
    print("Answer:", " ".join(answer))


# -----------------------------------
# MAIN GAME LOGIC
# -----------------------------------
def main():
    # Randomly select a word from the word list
    # Convert it to lowercase for consistent comparison
    answer = random.choice(words).lower()

    # Create a list of underscores (_) with the same length as the answer
    # This will be updated as the player guesses correctly
    hint = ["_"] * len(answer)

    # Counter for wrong guesses
    wrong_guesses = 0

    # A set to store letters that have already been guessed
    # Sets automatically prevent duplicate entries
    guessed_letters = set()

    # Maximum allowed wrong guesses
    # This is determined by the number of Hangman stages available
    max_wrong = len(hangman_art) - 1

    # Infinite loop that runs until the player wins or loses
    while True:
        # Display the current Hangman drawing
        display_man(wrong_guesses)

        # Display the current state of the word hint
        display_hint(hint)

        # Ask the player to guess a letter
        guess = input("Enter a letter: ").lower()

        # -----------------------------------
        # INPUT VALIDATION
        # -----------------------------------

        # Check if the input is exactly one alphabetical character
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Enter a single letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'.")
            continue

        # Add the valid guess to the set of guessed letters
        guessed_letters.add(guess)

        # -----------------------------------
        # CHECK THE GUESS
        # -----------------------------------

        # If the guessed letter is in the answer word
        if guess in answer:
            # Loop through the answer to reveal all matching letters
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            # Increment wrong guess count if the letter is not in the word
            wrong_guesses += 1
            print("❌ Wrong guess!")

        # -----------------------------------
        # WIN CONDITION
        # -----------------------------------

        # If there are no underscores left, the player has guessed the word
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("🎉 YOU WIN!")
            break

        # -----------------------------------
        # LOSE CONDITION
        # -----------------------------------

        # If the number of wrong guesses reaches the maximum allowed
        if wrong_guesses >= max_wrong:
            display_man(wrong_guesses)
            display_answer(answer)
            print("💀 YOU LOSE!")
            break


# -----------------------------------
# PROGRAM ENTRY POINT
# -----------------------------------
# This ensures the game runs only when this file
# is executed directly, not when imported as a module
if __name__ == "__main__":
    main()
