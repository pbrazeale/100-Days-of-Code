import random 

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers?\n"))
nr_symbols = int(input("How many symbols?\n"))


# Easy done, but Didn't figure out HARD which is the real random
#password = ''
# holding= []

# for char in range(1, nr_letters + 1):
#     holding += random.choice(letters)
# for num in range(1, nr_numbers + 1):
#     holding += random.choice(numbers)
# for sym in range(1, nr_symbols + 1):
#     holding += random.choice(symbols)

# for i in range(1, len(holding) + 1):
#     password += random.choice(holding)


# print(f"Your new password is:\n{holding}")
# print(f"Your new password is:\n{password}")

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for num in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
for sym in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# -_- If I read random more, I would have found the suffle function LOL

random.shuffle(password_list)

password = ''

for i in range(0, len(password_list)):
    password += password_list[i]

print(f"Your new password is:\n{password}")