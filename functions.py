def login():
    print("_______________WELCOME_____________")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("Welcome, " + username)

login()

def calculator():
    firstNumber = float(input("Enter the first number: "))
    operations = input("Enter the operation (+, -, *, /): ")
    secondNumber = float(input("Enter the second number "))

    if(operations == "+"):
        answer = firstNumber + secondNumber
    elif(operations == "-"):
        answer = firstNumber - secondNumber
    elif(operations == "*"):
        answer = firstNumber * secondNumber
    elif(operations == "/"):
        answer = firstNumber / secondNumber
    else:
        print("Invalid. Please start again.")
    print("The answer is: " + str(answer))
    return answer

result = calculator() * 2
print("The answer when multiplied by 2 becomes: " + str(result))

