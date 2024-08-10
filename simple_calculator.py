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

calculator()