alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# target_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

todo = input("Welcome to the Caesar Cipher.\nDo you want to 'encode' or 'decode'?\n").lower()
shift = int(input("What is the number key?\nEnter '1-26':\n"))
message = input("What is the message?\n")

def rotate(lst, n):
    return lst[n:] + lst[:n]

def encrypt(todo, shift, message):
    if todo == "decode":
        shift = -shift
    
    target_alphabet = rotate(alphabet, shift)
    
    encoded_message = ""
    
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            encoded_message += target_alphabet[index]
        
    print(encoded_message)

encrypt(todo, shift, message)



