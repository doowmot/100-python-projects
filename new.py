def greet():
    name = input("What's your name? ")
    while True:
        try:
            age = int(input("How old are you? "))
            break
        except ValueError:
            print("Please enter a valid number for age.")
    
    print(f"Hello {name}. You are {age} years old.")
    return name, age

user_name, user_age = greet()

if (user_age > 25):
    print(f"{user_name}, you are old.")
else:
    print(f"{user_name}, you are young.")


