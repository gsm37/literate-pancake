import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("")

p1 = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
cpu = random.randint(0,2)
if p1 == 0:
    print(rock)
    if cpu == 0:
        print("Computer Chose:\n")
        print(rock)
        print("\nIt is a tie")
    if cpu == 1:
        print("Computer Chose:\n")
        print(paper)
        print("\nYou lose")
    if cpu == 2:
        print("Computer Chose:\n")
        print(scissors)
        print("\nYou win")

if p1 == 1:
    print(paper)
    if cpu == 0:
        print("Computer Chose:\n")
        print(rock)
        print("\nYou Win")
    if cpu == 1:
        print("Computer Chose:\n")
        print(paper)
        print("\nIt is a tie")
    if cpu == 2:
        print("Computer Chose:\n")
        print(scissors)
        print("\nYou lose")

if p1 == 2:
    print(scissors)
    if cpu == 0:
        print("Computer Chose:\n")
        print(rock)
        print("\nYou lose")
    if cpu == 1:
        print("Computer Chose:\n")
        print(paper)
        print("\nYou Win")
    if cpu == 2:
        print("Computer Chose:\n")
        print(scissors)
        print("\nIt is a tie")
