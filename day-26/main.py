# Comprehension List

# numbers = [1, 2, 3]

# new_list = []

# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# print(new_list)

# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]

# print(new_list)

# name = "Raunik"

# new_name = [letter for letter in name]
# print(new_name)

# new_range = [n * 2 for n in range(1,5)]
# print(new_range)

# names = ["Raunik", "Beth", "Alex", "Dave", "Carolina", "Freddie"]
# new_name = [name for name in names if len(name) < 5]
# print(new_name)

# names = ["Raunik", "Beth", "Alex", "Dave", "Carolina", "Freddie"]
# new_name = [name.upper() for name in names if len(name) > 5]
# print(new_name)

# Dictionary Comprehension


# import random


# names = ["Raunik", "Beth", "Alex", "Dave", "Carolina", "Freddie"]
# student_scores = {name: random.randint(20, 100) for name in names}

# print(student_scores)

# passed_student = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_student)

# import pandas


# student_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "score": [76, 56, 65]
# }

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop in data frame

# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # print(index)
#     # print(row)
#     print(row.student)
#     print(row.score)