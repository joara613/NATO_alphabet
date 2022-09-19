import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


def generate_phonetic():
    word = input("give me a word: ").upper()
    try:
        letter_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(letter_list)


generate_phonetic()