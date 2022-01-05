# This program is challenge to encode texts from the users input
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def caesar(entered_text, shift_amount, chosen_direction):
    """This function encrypts or decrypts the message by shifting each letter
        of the 'text' forwards or backwards in the alphabet by the shift
        amount and print the encrypted or decrypted text"""
    end_text = ""

    '''Check if the user wanted to encrypt or decrypt the message
     as per the 'direction' variable. if decode, then shift backward.'''
    if chosen_direction == "decode":
        shift_amount *= -1
    for char in entered_text:
        # if the user enters a number/symbol/space, only encode/decode the letter
        # and keep the number/symbol/space when the text is encoded/decoded.
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {chosen_direction}d result : {end_text}")


# Print the logo from art.py when the program starts.
print(logo)

# def encrypt_message(plain_text, shift_amount):
#     """This function encrypts the message by shifting each letter
#      of the 'text' forwards in the alphabet by the shift amount
#      and print the encrypted text"""
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded or encrypted text is {cipher_text}")
#
#
# def decrypt_message(cipher_text, shift_amount):
#     """This function decrypts the message by shifting each letter
#      of the 'text' backwards in the alphabet by the shift amount
#      and print the decrypted text"""
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded or decrypted text is {plain_text}")
#
#
# '''Check if the user wanted to encrypt or decrypt the message
# as per the 'direction' variable. Then call the correct function
# as per the direction entered. '''
# if direction == "encode":
#     encrypt_message(plain_text=text, shift_amount=shift)
# else:
#     decrypt_message(cipher_text=text, shift_amount=shift)

# Ask the user if they want to restart the cipher program
should_continue = True
while should_continue:
    # User's inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Allow the program to keep working even if the user enters
    # a shift number > 26 (number of letters in the alphabet).
    # Then call the function, passing over the input values.
    shift = shift % 26
    caesar(entered_text=text, shift_amount=shift, chosen_direction=direction)

    # If the user types 'no' the program should end. Otherwise, the user
    # is asked for the direction/text/shift again and the caesar() function is called again.
    result = input("Type 'yes' if you wanna go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye!")

