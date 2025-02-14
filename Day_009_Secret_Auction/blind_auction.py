#print ascii art for bidding
print("Welcome to the secret auction program.")

bids = {}
highest_bid = 0
highest_bidder = 0

bidding_status = True

# Starts loop again with name, bid, other bidders
i = 1
while bidding_status:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    flag = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    bids[i] = [name, bid]
    
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = i

    i += 1
        
    if flag == 'yes':
        #this will clear screen.
        print("\n" * 100)
    elif flag == 'no':
        bidding_status = False




#no, leads to
print(f"The winner is {bids[highest_bidder][0]} with a bid of ${bids[highest_bidder][1]}.")
