def odd_or_even(number):
    #was '=' instead of '=='
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."
    

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            #was 4000 not 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    



# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        # was 'or' should be 'and'
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        #if instead of elif
        elif number % 3 == 0:
            print("Fizz")
        #if instead of elif
        elif number % 5 == 0:
            print("Buzz")
        else:
            #was '[number]' instead of 'number'
            print(number)
