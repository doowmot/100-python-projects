def add_pass():
    acc_name = input("Account Name: ")
    acc_pass = input("Password: ")
    print("--Successfully stored--")
    print("Account Name:", acc_name, "& Password:", acc_pass)

    with open ("passwords.txt", "a") as f:
        f.write(acc_name + "|" + acc_pass + "\n")

def view_pass():
    with open ("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, passw = data.split("|")
            print("User:", name, "& Password:", passw)

while True:
    mode = input("Would you like to 'add' a new login or 'view' existing ones? Press 'Q' to quit.  ").lower()
    if mode == 'q':
        break
    elif mode == "add":
        add_pass()
    elif mode == "view":
        view_pass()
    else:
        print("Please enter valid input.")
        continue

