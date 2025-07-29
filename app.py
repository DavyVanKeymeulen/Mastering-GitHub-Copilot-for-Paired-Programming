
# Rock-Paper-Scissors Minigame
# The winner of the game is determined by three simple rules:
# Rock beats scissors. Scissors beat paper. Paper beats rock.
# The computer will be your opponent and can randomly choose one of the elements (rock, paper, or scissors).
# Your game interaction will be through the console (Terminal).

import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(player, computer):
    """Determine the winner based on the rules."""
    if player == computer:
        return 'tie'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return 'win'
    else:
        return 'lose'

def main():
    print("Welcome to Rock-Paper-Scissors!")
    rounds = 0
    wins = 0
    while True:
        player = input("Choose rock, paper, or scissors: ").strip().lower()
        if player not in ['rock', 'paper', 'scissors']:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue
        computer = get_computer_choice()
        print(f"Computer chose: {computer}")
        result = get_winner(player, computer)
        if result == 'win':
            print("You win!")
            wins += 1
        elif result == 'lose':
            print("You lose!")
        else:
            print("It's a tie!")
        rounds += 1
        again = input("Play again? (yes/no): ").strip().lower()
        if again != 'yes':
            break
    print(f"Game over! You won {wins} out of {rounds} rounds.")

if __name__ == "__main__":
    main()