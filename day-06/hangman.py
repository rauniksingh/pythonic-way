import random
from hangman_art import stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
for char in chosen_word:
    placeholder += '_'

print(placeholder)

game_over = False
correct_letters = [];
lives = 6

while not game_over:

    guess = input("Guess the letter: ").lower()
    print(guess)

    display = ''

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
            print(f"You already guessed {letter}")
        else:
            display += '_'
    
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"--------- You have {lives} left")
        if lives == 0:
            game_over = True
            print("You loose!")

    if "_" not in display:
        print("You win!")
        game_over = True
    
    print(stages[lives])