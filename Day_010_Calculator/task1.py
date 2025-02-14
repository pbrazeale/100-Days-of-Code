print("Welcome to your calculator")

number1 = int(0)
def calculate():
    global number1
    while True:
        operation = input("Pick an operation: ")
        number2 = int(input("What is the second number?: "))

        if operation == "+":
            solution = number1 + number2
        elif operation == "-":
            solution = number1 - number2    
        elif operation == "*":
            solution = number1 * number2
        elif operation == "/":
            solution = number1 / number2
        else:
            return step_one()

        print(f"{number1} {operation} {number2} = {solution}")
        yn = input(f"Type 'y' to continue calculating with {solution}, or type 'n' to start a new calculation\n")

        if yn == 'n':
            return step_one()
        else:
            number1 = solution

def step_one():
    global number1
    number1 = int(input("What is the first number?: "))
    print("+")
    print("-")
    print("*")
    print("/")
    calculate()

step_one()