# SILENT AUCTIONING PROGRAM.
#DAY 9 PROJECT 
# AUTHOR LAWRENCE
# VERSION NO: 001
# LICENCE FREE TO USE.
#HAVE FUN

#FLOW CHART
    # 1. GET USER TO ENTER THE NAME AND BID PRICE
    # 2. LOOP UNTILL YOU GET ALL USERS WITH BIDS
    # 3. CRTL C TO CANCEL OTHERWISE LET USERS KEEP
    #  INPUTING VALUES
    # 4. END OF ENTRY DISPLAY THE WINNER HIGHEST BIDDER.
    
import getpass
dictionary = {}
bids = []

def get_input():
    print(
            f"""   WELCOME TO SILENT BIDDER \n   PRESS CONTROL C TO CANCEL\n   Your Bid is Private.\n   Press enter after Amount
             """
        )
    user_entry = str(input("Enter User Name: "))
    # users.append(user_entry)

    user_bid = int(getpass.getpass("How much for the item? :"))
    bids.append(user_bid) 
    dictionary[user_entry] = user_bid

def get_index_and_name():
# IT WILL GET INDEX OF THE MAXIMUM VALUE
# BY SORTING THE VALUES OF THE BIDS LIST 
# AND GETTING THE FIRST VALUE OF THAT LIST
    bids.sort(reverse=True)
    return bids[0]

def highest_bidder():
    #FROM THE DICTIONARY WE NEED TO LOOP TO GET THE NAME
    # OF THE HIGHEST BIDDER.
    for k,v in dictionary.items():
        if v == get_index_and_name():
            print("\n \n======================")
            print(f"\n  Bid Amount: ${bids[0]}")
            print(f"  {k} Won the Bid")
            print("\n======================")
            

if __name__ == "__main__":
    try:
        while True:
            get_input()
    except KeyboardInterrupt:
        highest_bidder()