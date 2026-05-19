import auction_art;

print(auction_art.hammer, "\n" * 5)

def find_highest_bidder(bids):
    # highest_bid = 0
    winner = '';

    winner = max(bids, key=bids.get)

    # for bid in bids:
    #     bid_amount = bids[bid]
    #     if bid_amount > highest_bid:
    #         highest_bid = bid_amount
    #         winner = bid
    
    print(f"The winner is {winner} with a bid of ${bids[winner]}")

bids = {}

continue_bidding = True

while continue_bidding == True:
    name = input("What is your name?: ")

    bid_price = int(input("What is your bid?: $"))

    bids[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.").lower()

    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        print("\n" * 20)

