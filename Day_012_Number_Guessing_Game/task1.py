#https://pypi.org/project/art/
from art import *
import random


def number_generation():
    target_number = random.randint(1, 100)
    return target_number

def attempts(lives):
    print(f"You have {lives} attempts remaining to guess the number.")

def guessing(difficulty):
    lives = 0

    if difficulty == 'hard':
        lives = 5
    else:
        lives = 10
    
    # target_number = number_generation()
    target_number = 23

    player_won = False
    
    attempts(lives)
    
    while lives > 0:    
        player_guess = int(input("Make a guess:  "))
        
        if player_guess > target_number:
            print("Too High.\nGuess again.")
            lives -= 1
            attempts(lives)
        elif player_guess < target_number:
            print("Too Low.\nGuess again.")
            lives -= 1
            attempts(lives)
        else:
            print("You Win!")
            lives = 0
            player_won = True
        
    if player_won == False:
        print("You lose.")
    
    play_agian = input("Play again? Type 'yes' or 'no': ").lower()
    if play_agian == 'yes':
        start_game()
        


def start_game():
    print(text2art("Guess The Number", "Cyber Large"))
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    guessing(difficulty)

start_game()