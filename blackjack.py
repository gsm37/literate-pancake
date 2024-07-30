#Basic BlackJack Game
#cards have equal chance of spawning in hand
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(logo)

def Blackjack():
    p1 = []
    dealer = []
    for i in range(2):
        card = random.choice(cards)
        p1.append(card)
        score = sum(p1)
    print(f"Your cards: {p1}, current score: {score}")

    dealer_card = random.choice(cards)
    dealer.append(dealer_card)
    dealer_score = dealer_card
    print(f"Computer's first card: {dealer}")

    more_cards = True
    while more_cards:
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == 'y':
            card = random.choice(cards)
            p1.append(card)
            score = sum(p1)
            print(f"Your cards: {p1}, Your score {score}")
            print(f"Dealers first card: {dealer}")
            if score > 21 and 11 in p1:
                position =  p1.index(11)
                p1[position] = 1
                score = sum(p1)
            if score > 21:
                print(f"Your score: {score}")
                print("You Lose!")
                more_cards = False
        if  choice == 'n':
            while dealer_score < 17:
                dealer_card = random.choice(cards)
                dealer.append(dealer_card)
                dealer_score = sum(dealer)

            if score > dealer_score or dealer_score > 21:
                print(f"Your final hand: {p1}, final score: {score}")
                print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")
                print("You Win!")
            elif score == dealer_score:
                print(f"Your final hand: {p1}, final score: {score}")
                print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")
                print("It's a draw stand down!")
            elif score == 21:
                if score == dealer_score:
                    print(f"Your final hand: {p1}, final score: {score}")
                    print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")
                    print("It's a draw stand down!")
                else:
                    print(f"Your final hand: {p1}, final score: {score}")
                    print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")
                    print("You Win!")
            else:
                print(f"Your final hand: {p1}, final score: {score}")
                print(f"Dealer's final hand: {dealer}, final score: {dealer_score}")
                print("You Lose!")
            more_cards = False

continue_game = True
while continue_game:
    choice = input("\n\n\n\nWould you like to play a game of BlackJack ? 'y' or 'n'").lower()
    if choice == 'y':
        Blackjack()
    elif choice == 'n':
        print("Exiting Program\nGoodbye")
        continue_game = False
    else:
        print("Error wrong input\nProgram terminating")
        continue_game = False



