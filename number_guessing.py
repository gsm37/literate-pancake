import random
logo = r'''

  _   _       _   _   __  __     ____  U _____ u   ____           ____     _   _ U _____ u ____    ____                  _   _     ____   
 | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u     U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      ___     | \ |"| U /"___|u 
<|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/     \| |  _ / \| |\| | |  _|" <\___ \/<\___ \/      |_"_|   <|  \| |>\| |  _ / 
U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <        | |_| |   | |_| | | |___  u___) | u___) |       | |    U| |\  |u | |_| |  
 |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\        \____|  <<\___/  |_____| |____/>>|____/>>    U/| |\u   |_| \_|   \____|  
 ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_       _)(|_  (__) )(   <<   >>  )(  (__))(  (__).-,_|___|_,-.||   \\,-._)(|_   
 (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__)     (__)__)     (__) (__) (__)(__)    (__)      \_)-' '-(_/ (_")  (_/(__)__)  
'''
def game(tries):
    print("I'm thinking of a Number between 1 and 100")
    num = random.randint(1, 100)
    #print(num)

    while tries != 0:
        print(f"you have {tries} attempts to guess the number ")
        guess = int(input("Make a guess: "))
        if guess == num:
            print("You Win!\n")
            break
        elif guess > num:
            tries -= 1
            if tries == 0:
                print("Too High\nyou Lose")
            else:
                print("Too High\nGuess again\n")
        elif guess < num:
            tries -= 1
            if tries == 0:
                print("Too Low\nyou Lose")
            else:
                print("Too Low\nGuess again\n")




continue_game = True
print(logo)
print("welcome to the number guessing game!")

while continue_game:
    difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        tries = 10
        game(tries)
    elif difficulty == 'hard':
        tries = 5
        game(tries)
    else:
        print("error wrong input")

    again = input("Would you like to play again? 'yes' or 'no'").lower()
    print("\n\n\n\n\n")
    if again == 'yes':
        print("\n")
    else:
        print("Goodbye")
        continue_game = False