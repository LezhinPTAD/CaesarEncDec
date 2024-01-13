# Colong module mati aja
# By lezhin

from time import sleep
import string

alphabet = string.ascii_lowercase

def decrypt():

    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("Masukkan text yang ingin kamu dekripsi: ").strip()
    print()
    key = int(input("Masukkan kunci untuk dekripsi: "))

    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("\nSedang meng-dekripsi text mu...\n")
    sleep(2)
    print("Hampir selesai...\n")
    sleep(2)
    print(f"Text terdekripsi mu adalah: {decrypted_message}")
