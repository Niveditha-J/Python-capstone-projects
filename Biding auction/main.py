from art import logo
print(logo)
bid={}
bidding_finish=False

def find_highest_bidder(bidding_record):
    highest_amount=0
    winner=""
    for bidder in bidding_record:
        bidding_amount=bidding_record[bidder]
        if bidding_amount>highest_amount:
            highest_amount=bidding_amount
            winner=bidder
    print(f"The winner is {winner} with bid amount {highest_amount}")

while not bidding_finish:
    Name=input("What is your name: ")
    price=int(input("Waht is your bid price: ₹"))
    bid[Name]=price
    should_continue=input("Are there any other user next.Type 'yes' or 'no' ")
    if should_continue=="no":
        bidding_finish=True
        find_highest_bidder(bid)
    elif should_continue=="yes":
        bid.clear()
        
        

    

