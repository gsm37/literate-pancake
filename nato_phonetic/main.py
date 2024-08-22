import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row["letter"]:row["code"] for (index, row) in df.iterrows()}

def nato_phonetic(word):
    wrld_lst = [dict.get(keys) for letter in word for keys in dict.keys() if letter == keys.lower()]
    return wrld_lst


#print(dict)


word = input("Enter a word: ")
lst = nato_phonetic(word)
print(lst)




