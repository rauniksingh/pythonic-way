# import random
# import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.my_favourite_number)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# random_heads_or_tails = random.randint(0, 1)
# if random_heads_or_tails == 0:
#   print("Heads")
# else:
#   print("Tails")  

# friends = ['Alice', "Bob", "Charlie"]

# friends.extend(['Raunik', "Peter"]);

# print(friends)

# # 1st Option
# print(random.choice(friends))

# # 2nd option
# random_index = random.randint(0, 4)
# print(friends[random_index])

# # 3rd option
# num_of_friends = len(friends) - 1;
# index = random.randint(0, num_of_friends)
# print(friends[index])

import random

rock = '''
      __
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) '''

paper = '''     
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
 '''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''';

game_images = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"You choose:\n {user_input}")
print(game_images[user_input])

computer_input = random.randint(0, 2);
print(f"Computer choose: {computer_input}")
print(game_images[computer_input])

if user_input >= 3 or user_input < 0:
  print("You choose invalid number. You loose")
elif user_input == 0 and computer_input == 2:
  print("You win!")
elif computer_input == 0 and user_input == 2:
  print("You lose!")  
elif computer_input > user_input:
  print("You lose!")
elif user_input > computer_input:
  print("You win!")
elif user_input == computer_input:
  print("It's a draw")