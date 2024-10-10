import tkinter
import customtkinter
import string
import secrets

# functions
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation 

    password_len = int(input("Enter the password length: "))
    has_letters = input("Do you want to include letters? (Y/N): ").lower() == "y"
    has_digits = input("Do you want to include numbers? (Y/N): ").lower() == "y"
    has_special_chars = input("Do you want to include special characters? (Y/N): ").lower() == "y"

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

def copy_password():
    pass

def save_password():
    pass

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# create frame
root = customtkinter.CTk()
root.geometry("720x720")
root.title("Password Generator 1.0")

# add title to program
title = customtkinter.CTkLabel(master=root, text="Password Generator 1.0", font=("Roboto",24))
title.pack(padx=10, pady=12)

# add user input
password_len = customtkinter.CTkEntry(master=root, placeholder_text="Enter desired password length")
password_len.pack(padx=10, pady=12) 

inc_letters = customtkinter.CTkCheckBox(master=root, text="Include letters?")
inc_letters.pack(padx=10, pady=12)

inc_numbers = customtkinter.CTkCheckBox(master=root, text="Include numbers?")
inc_numbers.pack(padx=10, pady=12)

inc_special_char = inc_numbers = customtkinter.CTkCheckBox(master=root, text="Include special characters?")
inc_special_char.pack(padx=10, pady=12)

# user submits
generate_password = customtkinter.CTkButton(master=root, text="Generate")
generate_password.pack(padx=10, pady=12)

password = customtkinter.CTkEntry(master=root, placeholder_text="'password is...'")
password.pack(padx=10, pady=12) 

copy_password = customtkinter.CTkButton(master=root, text="Copy", command=copy_password)
copy_password.pack(padx=10, pady=12)

save_password = customtkinter.CTkButton(master=root, text="Save", command=save_password)
save_password.pack(padx=10, pady=12)

# run program
root.mainloop()



# keeping for reference

    # entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    # frame = customtkinter.CTkFrame(master=root)
    # frame.pack(padx=60, pady=20, fill="both", expand=True)