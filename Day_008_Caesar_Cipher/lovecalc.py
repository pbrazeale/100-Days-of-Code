def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    true_word = "true"
    love_word = "love"
    
    true_number = 0
    love_number = 0
    for n in name1:
        if n in true_word:
            true_number += 1
    for n in name2:
        if n in true_word:
            true_number += 1
    for n in name1:
        if n in love_word:
            love_number += 1
    for n in name2:
        if n in love_word:
            love_number += 1

    print(f"{true_number}{love_number}")

calculate_love_score("Kanye West", "Kim Kardashian")