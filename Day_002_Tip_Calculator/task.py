total_bill = input("Welcome to the tip calculator!\nWhat was the total bill? $")
tip_precent = input("How much tip would you like to give? 10, 12, or 15? ")
people_split = input("How many people to split the bill? ")

print(f"Each person should pay: ${round(float(total_bill) * (1 + float(tip_precent) * .01) / float(people_split), 2)}")
