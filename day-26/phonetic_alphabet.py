import pandas

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data_frame)

new_dict = {row['letter']: row['code'] for (index, row) in data_frame.iterrows()}
# print(new_dict)

user_word = input("Enter a word: ").upper()

# for word in user_word:
#     print(new_dict[word])

output_list = [new_dict[name] for name in user_word]
print(output_list)