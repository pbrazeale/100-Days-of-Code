print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

total = 0

if size == 's':
    total += 15
elif size == 'm':
    total += 20
else:
    total += 25

if pepperoni == 'y':
    if total >= 20:
        total += 3
    else:
        total += 2

if extra_cheese == 's':
    total += 1

print(f"Your subtotal is ${total}.00")