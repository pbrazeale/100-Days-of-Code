import random

cards = [
    "A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
    "A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
    "A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
    "A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
]
count = {"A": 11, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10,}

players_cards = []
dealers_cards = []
card_count = 0
player_total = 0
dealer_total = 0

def dealer_score():
    global dealer_total, cards, card_count
    print(f"Dealer shows {dealers_cards}")
    dealer_total = count[dealers_cards[0]] + count[dealers_cards[1]]
    
    if dealer_total > player_total:
        print("You lose.")
    
    while dealer_total < 17:
        dealers_cards.append(cards[card_count])
        print(f"Dealer hits {dealers_cards}")
        if dealer_total > 11 and cards[card_count] == "A":
            dealer_total += 1
        else:
            dealer_total += count[dealers_cards[-1]]        
        card_count += 1

    if dealer_total > 21:
        print("You win!")
    elif dealer_total < player_total:
        print("You win!")
    elif dealer_total == player_total: 
        print("PUSH")
    else:
        print("You lose.")
    
    play()


def player_score():
    global player_total
    aces = 0
    for n in players_cards:
        if n == "A":
            aces += 1
        else:
            player_total += count[n]
    while aces > 0:
        if player_total <= 10:
            player_total += 11
            aces -= 1
        elif player_total > 10:
            player_total += 1
            aces -= 1
    dealer_score()   

def hit():
    global card_count, cards    
    next_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if next_card == 'y':
        players_cards.append(cards[card_count])
        print(players_cards)
        card_count += 1
        hit()
    else:
        player_score()

def play():
    global players_cards, dealers_cards, player_total, dealer_total, cards
    player_total = 0
    dealer_total = 0
    deal = input("Do you wnat to play blackjack? Type 'y' or 'n': ").lower()
    if deal == "y":
        random.shuffle(cards)
        players_cards = [cards[0], cards[1]]
        dealers_cards = [cards[2], cards[3]]
        print(f"Your cards: {players_cards}")
        print(f"Computer's first card: {dealers_cards[0]}")
        
        dealer_total = count[dealers_cards[0]] + count[dealers_cards[1]]
        player_toal = count[players_cards[0]] + count[players_cards[1]]
        if player_toal == 21:
            if dealer_total == player_toal:
                print(f"Computer shows {dealers_cards} you PUSH.")
            else:
                print("BlackJack, you WIN!")
        if dealer_total == 21:
            print(dealers_cards)
            print("Computer shows 21, you LOSE")
        
        hit()
    else: 
        play()

play()