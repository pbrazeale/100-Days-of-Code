from art import *
import random

current_score = 0

followers = {
    1300: "Musician",
    1000: "Author",
}

def logo():
    print(text2art("Higher", "Cyber Large"))
    print(text2art("Lower", "Cyber Large"))

def vs():
    print(text2art("Vs.", "Cyber Large"))

def score():
    global current_score
    current_score += 1
    print(f"You're Right! Current Score: {current_score}.")

def option_a(a_value):
    if a_value == 0:
        a_value = int(random.choice(list(followers)))
    print(f"Compare A: {followers[a_value]}")
    return a_value

def option_b(b_value, a_value):
    b_value = int(random.choice(list(followers)))
    while b_value == a_value:
        b_value = int(random.choice(list(followers)))        
    print(f"Against B: {followers[b_value]}")
    return b_value

def end_game():
    logo()
    print(f"Sorry, that's wrong. Final score: {current_score}")

def test_answer(player_guess, correct_answer, a_value, b_value):
    global current_score
    if player_guess == correct_answer:
        if player_guess == "a":
            current_score += 1
            game(a_value)
        else:
            current_score += 1
            game(b_value)
    else:
        end_game()

def game(past):
    global current_score
    logo()
    
    if current_score > 0:
        print(f"You're right! Current Score: {current_score}")
    
    a_value = past
    a_value = option_a(a_value)
    vs()
    b_value = option_b(0, a_value)
    
    player_guess = input("Who has more followers? Type 'A' or 'B':  ").lower()

    if a_value > b_value:
        correct_answer = "a"
    else:
        correct_answer = "b"

    test_answer(player_guess, correct_answer, a_value, b_value)

game(0)