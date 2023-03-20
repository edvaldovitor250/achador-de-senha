import random
import os

your_pwd = input("Digite uma senha: ")

pwd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
       'm', 'n', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

pw = ""

while (pw != your_pwd[::-1]):
    pw = ""
    for letter in range(len(your_pwd)):
        guess_pwd = pwd[random.randint(0, len(pwd)-1)]
        pw = str(guess_pwd)+str(pw)
        os.system("cls")
        print("Tentando senha:", pw)

print("Sua senha é", pw)
