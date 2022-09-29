import pandas
import csv
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
# with open('nato_phonetic_alphabet.csv') as f:
#     nato_dict = dict(filter(None, csv.reader(f)))
#     nato_dict2 = {letter:code for (letter, code) in nato_dict.items()}

data = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in user_input]
print(output_list)




# input_size = len(user_input)
# nato_data_frame = pandas.DataFrame(nato_dict2)
# counter = 0
# output_nato = []
# while counter != input_size:
#     user_input[counter]
