# coding = utf-8
# Author: Celine
# Date: 2023/4/6 21:45

from replit import clear
import art

bids = {}


def find_highest_bidder(bidding_record):
    highest_price = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if highest_price <= bid_amount:
            highest_price = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_price}.")


print(art.logo)
print("Welcome to the secret auction program.")

bidding_finished = False
while not bidding_finished:
    name = input("What's your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price

    others = input("Are there any other bidders? Type 'yes' or 'no'.")
    clear()
    if others == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif others == "yes":
        clear()
