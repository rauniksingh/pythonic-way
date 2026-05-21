# from random import randint
# Bug code
# dice_images = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
# dice_num = randint(1, 6)

# print(dice_images[dice_num])

#  Correct code
# dice_images = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
# dice_num = randint(0, 5)

# print(dice_images[dice_num])

# Bug Code
# year = int(input("What's your year of birth?: "))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# Bug fixed code
# year = int(input("What's your year of birth?: "))

# if year >= 1980 and year <= 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# try:
#     age = int(input("How old are you?: "))
# except ValueError:
#     print("Invalid Input. Try with number")
#     age = int(input("How old are you?: "))

# if age > 18:
#     print(f"You can drive at age {age}")


# Bug code
# word_per_page = 0
# pages = int(input("Number of pages: "))

# word_per_page == int(input("Number of word per page: "))

# total_word = pages * word_per_page
# print(total_word)

# Bug fixed code
word_per_page = 0
pages = int(input("Number of pages: "))

# print(word_per_page == int(input("Number of word per page: ")))
word_per_page = int(input("Number of word per page: "))
print(f"pages: {pages}")
print(f"word_per_page: {word_per_page}")

total_word = pages * word_per_page
print(total_word)