# # Conditional check
# print("Welcome to rollercoaster!")
# height = int(input("What is your height in cm ? "))

# if height >= 120:
#   print("You can ride the rollercoaster")
# else: 
#   print("Sorry you to grow taller before you can ride.")


# # Modular operator
# print(10 / 3)
# print(10 % 3)

# # Check if number is Odd or Even
# number_to_check = int(input("Enter a number: "))
# if number_to_check % 2 == 0:
#   print("Number is even")
# else:
#    print("Number is Odd")
# 

# Nested if else and elif
# print("Welcome to rollercoaster!")
# height = int(input("What is your height in cm ? "))

# if height >= 120:
#   age = int(input("Enter your age: "))
#   if age <= 12:
#     print("Please pay $5.")
#   elif age <= 18:
#     print("Please pay $7.")
#   else:  
#     print("Please pay $12")
# else: 
#   print("Sorry you to grow taller before you can ride.")


#  Pizza price calculator
# print("Welcome to python Pizza Delivery");
# size = input("What size pizza do you want? S, M, L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25

# pepperoni_for_small_pizza = 2
# pepperoni_for_medium_and_large_pizza = 3

# extra_cheese_price = 1

# bill = 0;

# if size == 'S':
#   bill += small_pizza
# elif size == 'M':
#   bill += medium_pizza
# else:
#   bill += large_pizza

# if pepperoni == 'Y':
#   if size == 'S':
#     bill += pepperoni_for_small_pizza
#   else:
#     bill += pepperoni_for_medium_and_large_pizza

# if extra_cheese == 'Y':
#   bill += extra_cheese_price

# print("Your final bill is: $", bill)

# print("Welcome to rollercoaster!")
# height = int(input("What is your height in cm? "))

# ticket_price = 0
# photo_price = 3

# if height < 120:
#   print("You are not eligiable for ride")
# else:
#   age = int(input("What is your age? "))
#   wanted_photo = input("Do you want photos? Y for yes and N for No ")
#   if age < 12 and wanted_photo == 'Y':
#     ticket_price += 5 + photo_price
#   elif age < 12 and wanted_photo == 'N':
#     ticket_price += 5
#   elif age >= 12 and age < 18 and wanted_photo == 'Y':
#      ticket_price += 7 + photo_price
#   elif age >= 12 and age < 18 and wanted_photo == 'N':
#     ticket_price += 7
#   elif age >= 18 and age < 45 and wanted_photo == 'Y':
#     ticket_price += 12 + photo_price
#   elif age >= 18 and age < 45 and wanted_photo == 'N':
#     ticket_price += 12
#   elif 45 <= age >= 55 and wanted_photo == 'Y':
#     ticket_price += 0

# print(f"The total bill is: ${ticket_price}")

print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
******************************************************************************* ''')

print("Welcome to Treasure Island")
print("Your mission is to find the Treasure")

choice1 = input('You\'re at crossroad, where you want to go?'
                'Type "left" or "right".').lower()

if choice1 == 'left':
  choice2 = input('You\'ve come to the lake, there a island in the middle of a lake.'
                  'Type "wait" to wait for boat or type "swim" to swin to the island. ').lower()
  if choice2 == 'wait':
    choice3 = input("You have arrived at the island unarmed. "
                     "There is a house with 3 doors. One red, "
                     "one yellow and one blue. "
                     "Which one will you choose? " ).lower()
    if choice3 == 'red':
      print("It's a room full of fire. Game Over")
    elif choice3 == 'yellow':
      print("You found the treasure. You Win!")
    elif choice3 == 'blue':
      print("You entered the room of beast. Game Over!")
    else:
      print("Wrong door. Game Over!")  
  else:
      print('Game Over!')
else:
  print('Game Over')