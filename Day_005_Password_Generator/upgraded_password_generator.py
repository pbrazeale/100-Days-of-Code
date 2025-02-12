import random 

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_length = 0

def passwordLength():
    global password_length
    password_length = int(input("How long should your password be?\n"))

def check_password_length():
    global password_length
    while True:
        if password_length < 12:
            print("Sorry, that password is too short.\n I recomend at least 12 random characters.\n Try again...")
            passwordLength()
        elif password_length > 20:
            print("Sorry, your password is too long!\nI rcomend a max of 20.\n 18 characters would take 7 Quindecillion years to crack...")
            passwordLength()
        else:
            break


def main():
    global password_length
    print("Welcome to the PassWord Generator!")
    passwordLength()
    check_password_length()
    
    num_letters = 1
    num_numbers = 1
    num_symbols = 1

    free_chars = password_length - (num_letters + num_numbers + num_symbols)

    num_letters += random.randint(0, free_chars)
    free_chars -= num_letters - 1
    num_numbers += random.randint(0, free_chars)
    free_chars -= num_numbers - 1
    num_symbols += free_chars

    password_list = []
    for char in range(0, num_letters):
        password_list.append(random.choice(letters))
    for num in range(0, num_numbers):
        password_list.append(random.choice(numbers))
    for sym in range(0, num_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = ''

    for i in range(0, len(password_list)):
        password += password_list[i]

    print(f"Your new password is:\n{password}")

main()
