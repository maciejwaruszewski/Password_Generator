import random

print('Password Generator')
characters = 'abcdefghijklmnoprstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}:"<>?|[];1234567890'

number = input('Amount of password to generate: ')
number = int(number)

print('Your password(s): ')

for pwd in range(number):
    passwords = ''
    for pwd in range(7,20):
        passwords += random.choice(characters)
    print(passwords)