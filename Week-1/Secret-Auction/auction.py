from art import logo

print(logo)

bids = {}
bid_continue = True


def highest_bid(bid_dictionary):
    highest = 0
    winner = ""
    for bid in bid_dictionary:
        bid_amount = int(bid_dictionary[bid])
        if bid_amount > highest:
            highest = bid_amount
            winner = bid
    print(f"The winner is {winner} with a bid of ${highest}")


while bid_continue:
    name = input("What is your name?: \n")
    bid_price = input("What is your bid?: \n")

    bids[name] = bid_price

    more_bids = input("Are there more bids?: y or n \n").lower()

    if more_bids == "n":
        bid_continue = False
        highest_bid(bids)