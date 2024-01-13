# Colong module mati aja
# By lezhin
from . import enkripsi, dekripsi
from time import sleep

def pemula():
        print("Script By Lezhin\n")
        sleep(1)
        print("Pilihlah apa yang ingin kamu lakukan")
        print("1. Enkripsi\n2. Dekripsi")
        pilih = input("Pilih angka : ")
        if pilih == "1":
                enkripsi.encrypt()
        elif pilih == "2":
                dekripsi.decrypt()
        else:
                print("Input salah!")
                pemula()
