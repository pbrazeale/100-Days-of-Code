alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' or 'decode'?\n").lower()
text = input("What is the message?\n")
shift = int(input("What is the number key?\nEnter '1-26':\n"))


def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        cipher_text += alphabet[shifted_position]
    
    print(f"Here is the encoded result: {cipher_text}")


encrypt(original_text=text, shift_amount=shift)