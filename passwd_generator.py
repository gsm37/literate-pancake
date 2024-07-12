import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passwd = ''
num_letters = len(letters)-1
num_numbers = len(numbers)-1
num_symbols = len(symbols)-1

total = nr_numbers+nr_symbols+nr_numbers
for i in range(total):
    rand_num = random.randint(0,num_numbers)
    rand_sym = random.randint(0,num_symbols)
    rand_lett = random.randint(0,num_letters)

    if nr_letters != 0:
        passwd+=letters[rand_lett]
        nr_letters-=1

    if nr_symbols != 0:
        passwd+=symbols[rand_sym]
        nr_symbols-=1

    if nr_numbers != 0:
        passwd+=numbers[rand_num]
        nr_numbers-=1

print(passwd)


