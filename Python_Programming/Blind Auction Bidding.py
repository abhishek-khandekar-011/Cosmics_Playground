def auc(dictionary):
    highest = 0
    winner = ""
    for bidder in dictionary:
        bid_amount = dictionary[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest}")


bids = {}

continue_bidding = True
while continue_bidding:
    name = input("Enter the name of your team: ").lower()
    price = int(input("Enter the amount to bid in the auction: "))
    bids[name] = price
    should_continue = input("Do you want to continue bidding? Yes or No ").lower()
    if should_continue == "no":
        continue_bidding = False
        auc(bids)
    elif should_continue == "yes":
        print("\n" * 5)  
