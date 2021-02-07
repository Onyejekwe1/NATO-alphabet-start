import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# # TODO 1. Create a dictionary in this format:

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")

nato_result = [nato_dict[word] for word in user_input.upper()]
print(nato_result)
