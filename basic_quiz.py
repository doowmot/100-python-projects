print("Welcome to the Quiz!")
print("You will be asked 5 questions. Let's see how you do..!")
print("______________________________________________________")

counter = 0
total = 5

q1 = input("Question 1: What is 5x5? ")
if q1 == '25':
    counter = counter + 1
    print("Correct")
else:
    print(f"Incorrect. The answer is {"25"}")

q2 = input("Question 2: What ocean connects North America with Europe? ").lower()
if q2 == 'atlantic':
    counter = counter + 1
    print("Correct")
else:
    print(f"Incorrect. The answer is {"Atlantic"}")

q3 = input("Question 3: What year did World War 2 End? ").lower()
if q3 == '1945':
    counter = counter + 1
    print("Correct")
else:
    print(f"Incorrect. The answer is {"1945"}")

q4 = input("Question 4: Who discovered the laws of gravity? ").lower()
if q4 == 'isaac newton':
    counter = counter + 1
    print("Correct")
else:
    print(f"Incorrect. The answer is {"Isaac Newton"}")

q5 = input("Question 5: Who painted the Mona Lisa? ").lower()
if q5 == 'leonardo da vinci':
    counter = counter + 1
    print("Correct")
else:
    print(f"Incorrect. The answer is {"Leonardo Da Vinci"}")


print("______________________________________________________")
print(f"You got {counter} out of {total} questions correct!")
print("______________________________________________________")


