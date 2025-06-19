# implementation python on Rock Paper Scissors game.  

import random  # for random functions

# Function to get computer's choice
def get_computer_choice():
    random_no = random.randint(1, 3)  # returns random integer value
    option = {1: "Rock", 2: "Paper", 3: "Scissors"}
    return option[random_no]

# Function to get user input
def get_user_input():
    user_input = input("Enter Rock/Paper/Scissors: ")
    return user_input.capitalize()  # ensures consistent format like "Rock"

# Function to determine the result
def get_result(user_pick, computer_pick):
    if user_pick == computer_pick:
        return "Draw"
    elif (
        (user_pick == "Rock" and computer_pick == "Scissors") or
        (user_pick == "Scissors" and computer_pick == "Paper") or
        (user_pick == "Paper" and computer_pick == "Rock")
    ):
        return "Win"
    else:
        return "Lose! Try again"

# Main game logic
computer_pick = get_computer_choice()
user_pick = get_user_input()
result = get_result(user_pick, computer_pick)

# Display result
print(f"Computer's pick: {computer_pick}")
print(f"Your pick: {user_pick}")
print(f"Result: You {result}")
