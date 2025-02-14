def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

opperator = {
    "+": add, 
    "-": sub, 
    "*": mul, 
    "/": div,
}

# # multiply 4 * 8 using dic

# print(opperator["*"](4,8))
print("Welcome to your calculator")
number1 = 0
def step1():
    global number1
    number1 = int(input("What is the first number?: "))
    print("+")
    print("-")
    print("*")
    print("/")
    return step2()
def step2():
    global number1
    operation = input("Pick an operation: ")
    number2 = int(input("What is the second number?: "))

    solution = opperator[operation](number1, number2)
    print(f"{number1} {operation} {number2} = {solution}")

    yn = input(f"Type 'y' to continue calculating with {solution}, or type 'n' to start a new calculation\n")

    if yn == "y":
        number1 = solution
        return step2()
    else:
        return step1()

step1()
