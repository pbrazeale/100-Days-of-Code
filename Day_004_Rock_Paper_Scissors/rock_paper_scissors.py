import random

player_choice = input("Choose Rock, Paper or Scissors:\n").lower()
computer_choice = random.randint(0, 2)

rock_paper_scissors = ["rock", "paper", "scissors"]

def win():
    print(f"{player_choice.capitalize()} beats {rock_paper_scissors[computer_choice]}\nYou WIN!")
def lose():
    print(f"{player_choice.capitalize()} loses to {rock_paper_scissors[computer_choice]}\nYou Lose.")
def tie():
    print(f"{player_choice.capitalize()} and {rock_paper_scissors[computer_choice]}\nYou Tie.")

if player_choice == rock_paper_scissors[computer_choice]:
    tie()

if player_choice == "rock":
    if computer_choice == 1:
        lose()
    if computer_choice == 2:
        win()

elif player_choice == "paper":
    if computer_choice == 0:
        win()
    if computer_choice == 2:
        lose()

else:
    if computer_choice == 0:
        lose()
    if computer_choice == 1:
        win()