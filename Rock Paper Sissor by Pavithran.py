from random import choice

def get_user_choice():
    while True:
        user_input = input("Rock, Paper, Scissors? (Type 'quit' to exit): ").capitalize()
        if user_input in ["Rock", "Paper", "Scissors", "Quit"]:
            return user_input
        else:
            print("Invalid input. Please enter 'Rock', 'Paper', 'Scissors', or 'Quit'.")

def determine_winner(player, computer):
    if player == computer:
        return "Tie!"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return f"You win! {player} beats {computer}."
    else:
        return f"You lose! {computer} beats {player}."

if __name__ == "__main__":
    choices = ["Rock", "Paper", "Scissors"]
    computer = choice(choices)

    while True:
        player = get_user_choice()
        
        if player == "Quit":
            print("You have quit the game!")
            break

        result = determine_winner(player, computer)
        print(result)

        computer = choice(choices)
