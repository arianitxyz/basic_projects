import random
import string

print('Welcome to the password generator')
chars = string.printable

number = int(input('Number of password to generate: '))
length = int(input('Length of the generated password is: '))

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)