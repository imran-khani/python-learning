# Simple Password generator

import random
import string


len_of_password = int(input("Enter length of passwrod you want to generate: "))

characters = string.ascii_lowercase

ask_uppercase = input("Include uppercase? (y/n): ")
if ask_uppercase == 'y':
    characters += string.ascii_uppercase

ask_digits = input("Include Digits? (y/n): ")
if ask_digits == 'y':
    characters += string.digits

ask_symbols = input("Include special characters (e.g. #,$,%)? (y/n): ").lower()
if ask_symbols == "y":
    characters += string.punctuation

# Generate Password
password = "".join(random.choice(characters) for _ in range(len_of_password))
print("Generated password:", password)
