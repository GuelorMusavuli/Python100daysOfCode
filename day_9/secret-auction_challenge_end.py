import os
from art import logo

# Show logo from art
print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    """
        Find the highest bid in the dictionary
        and declare them as the winner
    """
    highest_bid = 0
    winner = ""
    # bidding_record = {"John": 128, "Peter": 301}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Function to clear  output in the console
def clear(): os.system('cls')


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
