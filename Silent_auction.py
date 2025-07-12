import os

bids={}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def highest_bidder(bidding_rec):
    highest_bid=0
    winner=''
    for bidder in bidding_rec:
        bid_amt=bidding_rec[bidder]
        if bid_amt > highest_bid:
            highest_bid=bid_amt
            winner=bidder
    print(f"\n the winnner is {winner} with a bid of {highest_bid}")



bidding_finish=False

while not bidding_finish:
    name=input("enter the name of the bidder: ")
    bid=int(input("enter the amount to be bid: "))
    bids[name]=bid

    more_bidders=input("are there more bidders? [enter yes/no only] \n").lower()
    if more_bidders=='no':
        bidding_finish=True
        clear_screen()
        highest_bidder(bids)
    else:
        clear_screen()

