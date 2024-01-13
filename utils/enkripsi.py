# Nyolong module mati aja
# By lezhin

from time import sleep
import string

alphabet = string.ascii_lowercase

def encrypt():
    print("Welcome to Caesar Cipher Encryption.\n")
    decrypted_message = input("Masukkan text yang ingin kamu enkripsi: ").strip()
    print()

    key = int(input("Masukkan jarak untuk enkripsi: "))

    encrypted_message = ""

    for c in decrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position + key) % 26
            new_character = alphabet[new_position]
            encrypted_message += new_character
        else:
            encrypted_message += c

    print("\nSedang meng-enkripsi textmu...\n")
    sleep(2)
    print("Hampir selesai...\n")
    sleep(2)
    print(f"Text terenkripsi mu adalah: {encrypted_message}")
