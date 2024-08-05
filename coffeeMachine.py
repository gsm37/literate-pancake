import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
water = 300 #ml
milk = 200 #ml
coffee = 100 #g

amount = 0.00
def menu(amount):
    choice = input("what would you like? (espresso/latte/capuccino) or write report to see available ingredients: ").lower()
    if choice == 'report':
        print(str(water) + 'ml')
        print(str(milk) + 'ml')
        print(str(coffee) + 'g')
        print('Money: $' + str(amount))
        return choice, False
    elif choice not in MENU:
        print("Please Enter a valid choice (espresso/latte/cappuccino) or type 'report' to see available ingredients:\n ")
        return choice, False
    else:
        return choice, True

def calculate(choice,water,milk,coffee):
    if choice == 'espresso':
        if water >= MENU[choice]['ingredients']['water'] and coffee >= MENU[choice]['ingredients']['coffee']:
            water-=MENU[choice]['ingredients']['water']
            coffee-=MENU[choice]['ingredients']['coffee']
            return choice, water, milk, coffee, True
        else:
            print("Sorry, not enough ingredients for your coffee")
            return choice, water, milk, coffee, False

    elif water >= MENU[choice]['ingredients']['water'] and coffee >= MENU[choice]['ingredients']['coffee'] and milk >= MENU[choice]['ingredients']['milk']:
        water -= MENU[choice]['ingredients']['water']
        coffee -= MENU[choice]['ingredients']['coffee']
        milk-= MENU[choice]['ingredients']['milk']
        return choice, water, milk, coffee, True

    elif water < MENU[choice]['ingredients']['water'] and coffee < MENU[choice]['ingredients']['coffee'] and milk < MENU[choice]['ingredients']['milk']:
        print("Sorry, not enough ingredients for your coffee")
        return choice, water, milk, coffee, False


def price(choice,amount):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if amount >= MENU[choice]['cost']:
        total = amount - MENU[choice]['cost']
        total = round(total,2)
        return choice,total,True
    else:
        print("Sorry, not enough funds for coffee")
    return choice, amount, False

while True:
    selection, is_valid = menu(amount)
    #print(type(selection),type(is_valid))
    if is_valid:
        selection,water,milk,coffee,is_selected = calculate(selection,water,milk,coffee)
        if is_selected:
            selection,total, is_paid = price(selection,amount)
            if is_paid:
                print(f"here is your change ${total}")
                print(f"here is your {selection} enjoy!")
            else:
                #hit this if not enough money so customer sees the initial prompt again
                continue
        while True:
            another = input("would you like another coffee?: ")
            if another == 'yes':
                print("\n\n\n")
                break
            elif another == 'no':
                print("Goodbye")
                exit()
            else:
                print("Invalid choice please type yes for another coffee or no to exit the program\n")













