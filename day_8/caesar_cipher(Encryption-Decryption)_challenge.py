# This program is challenge to encode texts from the users input

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

# User's inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt_message(plain_text, shift_amount):
    """This function encrypts the message by shifting each letter
     of the 'text' forwards in the alphabet by the shift amount
     and print the encrypted text"""
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded or encrypted text is {cipher_text}")


def decrypt_message(cipher_text, shift_amount):
    """This function decrypts the message by shifting each letter
     of the 'text' backwards in the alphabet by the shift amount
     and print the decrypted text"""
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded or decrypted text is {plain_text}")


'''Check if the user wanted to encrypt or decrypt the message 
as per the 'direction' variable. Then call the correct function 
as per the direction entered. '''
if direction == "encode":
    encrypt_message(plain_text=text, shift_amount=shift)
else:
    decrypt_message(cipher_text=text, shift_amount=shift)
