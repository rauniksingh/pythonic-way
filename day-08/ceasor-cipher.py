alphabet = [
  "a","b","c","d","e","f","g","h","i","j","k","l","m",
  "n","o","p","q","r","s","t","u","v","w","x","y","z"
]

direction = input("Type 'encode' to encrypt, type 'decode' to decypt: \n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type shift number:\n"))

# def encrypt(original_text, shift_amount):
#     decrypted_text = ''
#     for char in original_text:
#         original_text_index = alphabet.index(char);
#         idx = original_text_index + shift_amount
#         if idx > len(alphabet):
#             idx %= len(alphabet)
        
#         decrypted_text += alphabet[idx]
    
#     print(decrypted_text);

# encrypt(text, shift)

# def decrypt(original_text, shift_amount):
#     output_text = ''
#     for char in original_text:
#         original_text_index = alphabet.index(char);
#         idx = original_text_index - shift_amount
#         if idx > len(alphabet):
#             idx %= len(alphabet)
        
#         output_text += alphabet[idx]
    
#     print(output_text);

# decrypt(text, shift)

def ceasor(original_text, shift_amount, direction):
    output_text = '';

    if direction == 'decode':
        shift_amount *= -1;

    for char in original_text:
        
        if char not in alphabet:
            output_text += char;
        else:
            original_text_index = alphabet.index(char);
            idx = original_text_index + shift_amount

            if idx > len(alphabet):
                idx %= len(alphabet)
            
            output_text += alphabet[idx]

    print(f"Here's your {direction}d text: {output_text}");

ceasor(text, shift, direction)

should_continue = True;

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decypt: \n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type shift number:\n"))

    ceasor(text, shift, direction)
    restart = input("Do you want to continue ? Type 'Yes' to continue or 'No' to exit \n")
    if restart == 'no':
        should_continue = False
        print("Good Bye!")
