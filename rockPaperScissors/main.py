import random

option = ("rock", "paper", "scissors")
player = None
computer = random.choice(option)
running = True

while running:

    while player not in option:
        player = input("Enter a choice (rock, paper, scissors): ")
    print(f"Player: {player}")
    print(f"Player: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")