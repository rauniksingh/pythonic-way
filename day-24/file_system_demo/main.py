with open("./Input/Letter/starting_letter.txt") as letter:
    letter_template = letter.read()
    
    with open("./Input/Names/invited_names.txt") as file:
        for name in file:
            print(name)
            cleaned_name = name.strip()
            new_invite = letter_template.replace("[name]", cleaned_name)

            with open(f"./Output/Ready_to_send/letter_for_{cleaned_name}.txt", "w") as invite:
                invite.write(new_invite)