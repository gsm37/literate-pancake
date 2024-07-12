print(r'''
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|

                           _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                 '-._'-.|| |' `_.-'
                    '-.||_/.-'             
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
while True:
    choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')
    if choice1 == 'left':
        choice2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
        if choice2 == 'wait':
            choice3 = input("You arrive to an island unharmed. There is a house with 3 door. One red, one yellow and one blue. Which colour do you choose?\n")
            if choice3 == 'red':
                print("Burned by fire.\nGame over.")
            elif choice3 == 'yellow':
                print("You found the treasure.\nYou Win!")
                print(r'''
                 _____ _____     
                |  __ \  __ \    
                | |  \/ |  \/___ 
                | | __| | __/ __|
                | |_\ \ |_\ \__ \
                \____/\____/___/
                ''')
            elif choice3 == 'blue':
                print("You were eaten by beasts.\nGame over.")
            else:
                print("Game Over")
        elif choice2 == 'swim':
            print("You were devoured by piranhas.\nGame over.")
        else:
            print("Game over")
    elif choice1 == 'right':
        print("You fell into a hole.\nGame over")
    else:
        print("You fell into a hole.\nGame over")

    choice = input("would you like to play again?\n")
    if choice == 'yes':
        continue
    else:
        print("Game over")
        break
