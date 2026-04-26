import random

def play_game():
    choices = ["stone", "paper", "scissors"]

    print("\n--- Stone Paper Scissors ---")
    user = input("Enter stone, paper, or scissors: ").lower()

    # Validate input
    if user not in choices:
        print("Invalid input! Try again.")
        return None

    computer = random.choice(choices)
    print("Computer chose:", computer)

    # Game logic
    if user == computer:
        print("It's a tie!")
        return 0
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        return 1
    else:
        print("Computer wins!")
        return -1