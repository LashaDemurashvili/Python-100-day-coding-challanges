"""
Day 9 - Beginner - Dictionaries, Nesting and the Secret Auction

Program: The Secret Auction

program Description:
flow_chart/structure.png
"""

from recources.art import logo

print(logo)

# bids - dictionary, which contains a pair of key value, key = "name", and value = "bids"
# for example
# {"lasha": 100}


# create new global empty dictionary
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record: dict):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is >> {winner} << with a bid of >> ${highest_bid} <<")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    # add new key: value - pair each iteration
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'y/yes or 'n/no': ")
    if should_continue == "n":
        bidding_finished = True
        find_highest_bidder(bids)
