import random

print("welcome to password generator")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()'

number = int(input("Enter number of passwords : "))

length = int(input('Your password length: '))

print('\n Your passwords : ')

for pwd in range(number) :
    passwords = ""
    for c in range(length) :
        passwords += random.choice(chars)
    print(passwords)