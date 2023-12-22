# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

placeholder = "[name]"
x = []

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read().splitlines()
    for name in names:
        x.append(name)

print(x)


for i in range(len(x)):
    p = ['l', 't', 'z']
    # if x[i].lower().startswith("l"):
    #     x[i] = x[i].upper()
    for j in p:
        if x[i][0].lower() == j:
            x[i] = x[i].upper()
        else:
            pass

print(x)

# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_content = letter_file.read()
#     for name in names:
#         name = name.strip()
#         new_letter = letter_content.replace(placeholder, name)
#         with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as complete_text:
#             complete_text.write(new_letter)
