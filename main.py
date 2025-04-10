import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dic = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        code_list = [alphabet_dic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(code_list)

generate_phonetic()