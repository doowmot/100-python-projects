import random
import string

def generate_password(min_length, numbers = True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation 

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria + has_special

    return password

pass_len = input("Enter the password length: ")
has_num = input("Do you want to include numbers? (Y/N): ").lower() == "y"
has_special = input("Do you want to include special characters? (Y/N): ").lower() == "y"

password = generate_password(pass_len, has_num, has_special)
print("Generated Password: ", password)