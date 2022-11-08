import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def test1():
    while True:
        word = input("Enter a word: ").upper()
        try:
            output_list = [phonetic_dict[letter] for letter in word]
        except KeyError:
            print("Sorry only letters can be typed !!!")
            continue
        else:
            print(output_list)
            break
# test1()


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters can be typed !!!")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
