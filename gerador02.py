import secrets
import string

your_pwd = input("Digite uma senha: ")

# Lista de caracteres permitidos para senhas
pwd = string.ascii_letters + string.digits + string.punctuation

pw = ""
max_attempts = 1000000
attempts = 0

while (pw != your_pwd[::-1]) and (attempts < max_attempts):
    pw = ""
    for letter in range(len(your_pwd)):
        guess_pwd = secrets.choice(pwd)
        pw = str(guess_pwd) + str(pw)
    print("Tentando senha:", pw)
    attempts += 1

if attempts < max_attempts:
    print("Sua senha é", pw)
else:
    print("Não foi possível adivinhar a senha dentro do limite de tentativas.")
