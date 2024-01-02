import pandas

# TODO 1. Create a dictionary in this format:

data = pandas.read_csv('nato_phonetic_alphabet.csv')
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(new_dict.keys())
# print(new_dict.values())
# print(new_dict.items())
# print(new_dict)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter the word: ").upper()
coded_name = [new_dict[i] for i in word if i in new_dict]
print(coded_name)


# test case
# lasha
# result -> ['Lima', 'Alfa', 'Sierra', 'Hotel', 'Alfa']