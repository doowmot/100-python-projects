import string
import secrets

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation 

password_len = int(input("Enter the password length: "))
has_letters = input("Do you want to include letters? (Y/N): ").lower() == "y"
has_digits = input("Do you want to include numbers? (Y/N): ").lower() == "y"
has_special_chars = input("Do you want to include special characters? (Y/N): ").lower() == "y"

# or press q to quit..?

char_pool = ''
if has_letters:
    char_pool += letters
if has_digits:
    char_pool += digits
if has_special_chars:
    char_pool += special_chars

if not char_pool:
    print("Error: You must select at least one character type.")
    exit()

password = ''.join(secrets.choice(char_pool) for _ in range(password_len))

print("Generated password:", password)

save_password = input("Would you like to store the password in a text file? (Y/N): ")

if save_password == "y":
    reference = input("Enter the name of the reference to store the password: ")
    with open('passwords.txt', 'a') as file:
        file.write(f"\nReference: {reference} | Password: {password}")
print(f"Password: '{password}' has been saved to passwords.txt under the reference '{reference}'")


# next task: make it interactive - add gui.