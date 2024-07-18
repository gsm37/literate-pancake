alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#encrypt function
#create an empty string and loop for each letter in the input text
#for each letter store the index of the using the alphabet list
#add the index with the shift number this will give you a new index
#check if the index is less than since we are subtracting and there are only 26 items in the list
#use the formula of caesars cipher when the index is small so we can get a new index in the range of the alphabet list
#with the new index we will grab the new letter from the alphabet list and add it to the empty string
def encrypt(text,shift):
    encrypt_mess = ''
    for letter in text:
        if letter in '1234567890!@#$%^&*()?' or letter == ' ':
            encrypt_mess+=letter
            continue
        index = alphabet.index(letter)
        #print(index)
        index+=shift
        #print(f"new index: {index}")
        if index > 25:
            index%=26
        encrypt_mess+=alphabet[index]
    print(f"Here is the encrypted message: {encrypt_mess}")

#decrypt function
#create an empty string and loop for each letter in the input text
#for each letter store the index of the using the alphabet list
#subtract the index with the shift number this will give you a new index
#check if the index is grater than 25 since there are 26 letters in the alphabet
# use the formula of caesars cipher when the index is large so we can get an index in the range of the alphabet list
#with the new index we will grab the new letter from the alphabet list and add it to the empty string
def decrypt(text, shift):
    decrypt_mess = ''
    for letter in text:
        if letter in '1234567890!@#$%^&*()?' or letter == ' ':
            decrypt_mess+=letter
            continue
        index = alphabet.index(letter)
        #print(index)
        index -= shift
        #print(f"new index: {index}")
        if index < 0:
            index %= 26
        decrypt_mess += alphabet[index]
    print(f"here is the decrypted message: {decrypt_mess}")

run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text,shift)
    again = input("would you like to encrypt/decrypt a meesage again?")
    if again == 'yes':
        print("\n")
    elif again == 'no':
        print("goodbye")
        run = False
