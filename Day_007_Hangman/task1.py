# Flowchart Programming
import random
# would form hangman-words import word_list

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives = 6 
# print(chosen_word)

placeholder=""

for letter in chosen_word:
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You already guessed: {correct_letters}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(f"Lives left: {lives}")
    print(display)

    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            print("***GAME OVER***")
            game_over = True
    
    if "_" not in display:
        print("*******You Win!*******")
        game_over = True
