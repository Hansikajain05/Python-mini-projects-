from game import play_game

def main():
    user_score = 0
    computer_score = 0

    while True:
        result = play_game()

        if result == 1:
            user_score += 1
        elif result == -1:
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()