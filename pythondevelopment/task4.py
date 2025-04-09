import random

def get_computer_choice():
    # Randomly choose rock, paper, or scissors for the computer
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    # Take user input for their choice
    while True:
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid input. Please choose either 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the rules of the game
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors game!")

    # Get user and computer choices
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine and display the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game
play_game()
