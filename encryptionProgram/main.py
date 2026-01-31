import random
import string

def main():
    # Character set
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)

    # Create key
    key = chars.copy()
    random.shuffle(key)

    # ENCRYPT
    plain_text = input("Enter a message to encrypt: ")
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    print("\nOriginal message :", plain_text)
    print("Encrypted message:", cipher_text)

    # DECRYPT
    cipher_input = input("\nEnter a message to decrypt: ")
    decrypted_text = ""

    for letter in cipher_input:
        index = key.index(letter)
        decrypted_text += chars[index]

    print("\nEncrypted message:", cipher_input)
    print("Decrypted message:", decrypted_text)


if __name__ == "__main__":
    main()
