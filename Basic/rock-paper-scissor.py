import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Enter rock, paper, or scissors: ").lower()
print("Computer:", computer)
if player == computer and player in choices:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif player == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("You lose!")
elif player == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid input. Please enter rock, paper, or scissors.")
