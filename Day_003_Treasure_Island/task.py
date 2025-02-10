from art import text2art
import sys

Art = text2art("Treasure Island", font="fraktur")
print(Art)

print("Welcome to Terasure Island.")
first_move = input("Would you like to go Left or Right?\n").lower()

if first_move != "left":
    print("You fell into a hole.\nGAME OVER")
    sys.exit()

second_move = input("You see a pool of water. Swim or Wait?\n").lower()

if second_move != "wait":
    print("You were attacked by a trout.\nGAME OVER")
    sys.exit()

third_move = input("You find yourslef in a room standing before three doors: Red, Yellow, and Blue.\nWhich door do you open? ").lower()

if third_move == "red":
    print("You were burned by fire.\nGAME OVER")
elif third_move == "blue":
    print("You were eaten by beasts.\nGAME OVER")
elif third_move == "yellow":
    print("You WIN!")
else:
    print("Game Over.")
    