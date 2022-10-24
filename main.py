alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

shift = shift % 26
#
# def encrypt(plain_text, shift_amount):
#     word = ""
#     for letter in plain_text:
#         x = alphabet.index(letter)
#         word += alphabet[x+shift_amount]
#     print(word)
#
# def decode(plain_text, shift_amount):
#     word = ""
#     for letter in plain_text:
#         x = alphabet.index(letter)
#         word += alphabet[x-shift_amount]
#     print(word)
#
#
# if direction == "decode":
#     decode(plain_text=text, shift_amount=shift)
# elif direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# else:
#     print("invalid")

# def caesar(direction, text, shift):
#     word = ""
#     if direction == "decode":
#         for letter in text:
#             x = alphabet.index(letter)
#             word += alphabet[x-shift]
#         print(word)
#     elif direction == "encode":
#         for letter in text:
#             x = alphabet.index(letter)
#             word += alphabet[x + shift]
#         print(word)
#
# caesar(direction, text, shift)

def caesar(direction, text, shift):
    word = ""
    for letter in text:
        if direction == "decode":
            if letter in alphabet:
                x = alphabet.index(letter)
                word += alphabet[x-shift]
            else:
                word += letter
        elif direction == "encode":
            if letter in alphabet:
                x = alphabet.index(letter)
                word += alphabet[x + shift]
            else:
                word += letter
    print(word)

    again = input("type yes to continue")
    if again == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)


caesar(direction, text, shift)



# plain_text = input("Type your message:\n").lower()
# shift_amount = int(input("Type the shift number:\n"))
# word = ""
# for letter in plain_text:
#     x = alphabet.index(letter)
#     word += alphabet[x+shift_amount]
# print(word)
