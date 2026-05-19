import random

letters = [
  "A","B","C","D","E","F","G","H","I","J","K","L","M",
  "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
  "a","b","c","d","e","f","g","h","i","j","k","l","m",
  "n","o","p","q","r","s","t","u","v","w","x","y","z"
]

numbers = ['0', '1', '2', '3', '4' , '5', '6', '7', '8', '9']

symbols = ["!",  "#", "$", "%", "&", "*", "(", ")", "+"]

print("Welcome to the Pypassword Generator")

nr_letters = int(input("How many letters you want in your password?\n"))
nr_symbols = int(input("How many symbol you would like?\n"))
nr_number = int(input("How many numbers you would like?\n"))

# password = ''

# # Easy Level
# for letter in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for symbol in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for number in range(1, nr_number + 1):
#   password += random.choice(numbers)

# print(password)

# Hard Level
password_list = []

for char in range(0, nr_letters):
  password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
  password_list.append(random.choice(symbols))

for char in range(0, nr_number):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = '';

for char in password_list:
  password += char


print(f"Your password is: {password}")