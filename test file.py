import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_choice(player):
    choice = input(f"{player}, enter your choice (rock, paper, scissors, lizard, spock): ").lower()
    while choice not in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
        print("Invalid choice. Please choose rock, paper, scissors, lizard, or spock.")
        choice = input(f"{player}, enter your choice (rock, paper, scissors, lizard, spock): ").lower()
    return choice


def determine_winner(choice1, choice2):
    winning_combinations = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }

    if choice1 == choice2:
        return "It's a tie!"
    elif choice2 in winning_combinations[choice1]:
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"


def play_game():
    clear_screen()
    print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")

    # Get choices from both players
    player1_choice = get_choice("Player 1")
    clear_screen()  # Clear the screen before Player 2 inputs their choice
    player2_choice = get_choice("Player 2")

    # Reveal choices
    print(f"\nPlayer 1 chose: {player1_choice}")
    print(f"Player 2 chose: {player2_choice}")

    # Determine and display the winner
    result = determine_winner(player1_choice, player2_choice)
    print(result)


if __name__ == "__main__":
    play_game()