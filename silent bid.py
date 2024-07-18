import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

contestants = {}
highest_bid = 0

def blind_bid():
    name = input("What is your name?: ")
    bid = int(input("what is your bid?: "))
    contestants[name] = bid


print(logo)
print("Welcome to the Silent auction")
more = True
highest_bidder = ""

while more:
    blind_bid()
    for key in contestants:
        if contestants[key] > highest_bid:
            highest_bidder = key
            highest_bid = contestants[key]

    add = input("Are there any other bidders? Type 'yes' or 'no'.")
    if add == 'yes':
        os.system('cls')
    elif add == 'no':
        print(f"\nWinner is {highest_bidder} with a bid of ${highest_bid}")
        more = False



