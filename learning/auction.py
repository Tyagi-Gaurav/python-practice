#!/usr/bin/python3

import art
#HINT: You can call clear() to clear the output in the console.

all_bids = {}

keep_going = True
max = 0
winner = ""
while keep_going:
    print(art.auction_logo)
    print("Welcome to the secret auction program. ")
    name = input("What is your name?:")
    bid = int(input("What's your bid?: $"))
    if bid > max:
      winner = name
    any_more = input("Are there any other bidders? Type 'yes' or 'no'.")

    all_bids[name] = bid

    if any_more == 'no':
        keep_going = False


print (f"The winner is {winner} with a bid of ${all_bids[winner]}")