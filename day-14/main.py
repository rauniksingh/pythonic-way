# Higher or lower project

import random
import data
import art

print(art.logo)
print("\n" * 4)

current_score = 0
# b_compare = random.choice(data.data)

def format_data(account):
    return f"{account['name']}, {account['description']}, from {account['country']}"

def play_game(current_score, b_compare):
    if current_score == 5:
        print(f"You won! Your score is {current_score}")
        exit()

    a_compare = random.choice(data.data)
    b_compare = random.choice(data.data)

    print(f"Compare A: {format_data(a_compare)}\n")

    print(art.vs)

    print(f"\n Against B: {format_data(b_compare)}\n")

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_input == 'a' and a_compare['follower_count'] > b_compare['follower_count']:
        current_score += 1
        print(f"You are right. Current score: {current_score}.\n")
        play_game(current_score, b_compare)
    elif user_input == 'a' and b_compare['follower_count'] > a_compare['follower_count']:
        print(f"Sorry, that's wrong. Final score: {current_score}\n")
    elif user_input == 'b' and b_compare['follower_count'] > a_compare['follower_count']:
        current_score += 1
        print(f"You are right. Current score: {current_score}.\n")
        play_game(current_score, b_compare)
    elif user_input == 'b' and a_compare['follower_count'] > b_compare['follower_count']:
        print(f"Sorry, that's wrong. Final score: {current_score}\n")
    elif a_compare['follower_count'] == b_compare['follower_count']:
        current_score += 1
        print(f"You are right. Current score: {current_score}.\n")
        play_game(current_score, b_compare)

play_game(current_score, b_compare)