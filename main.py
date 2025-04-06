import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dic = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}

word = input("Enter a word: ").upper()
code_list = [alphabet_dic[letter] for letter in word]
print(code_list)