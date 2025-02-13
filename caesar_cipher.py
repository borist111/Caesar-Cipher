import string
import art
print(art.logo)
alphabet = list(string.ascii_lowercase)


def caesar(some_text, some_shift, encode_or_decode):
    output = ""
    if encode_or_decode == 'decode':
        some_shift *= -1
    for letter in some_text:

        if letter not in alphabet:
            output += letter

        else:

            shifted_position = alphabet.index(letter) + some_shift
            shifted_position = shifted_position % len(alphabet)
            output += alphabet[shifted_position]

    print(f'{encode_or_decode}d result: {output}')


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' or 'no' if you want to go again.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
