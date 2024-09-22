import random

user_wins = 0
ai_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Please Type Rock/Paper/Scissors or press 'Q' to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2) # rock = 0, paper = 1, scissors = 2
    ai_input = options[random_number]
    print(f"AI chose {ai_input}")

    if user_input == "rock" and ai_input == "scissors":
        print("You win!")
        user_wins +=1
    
    elif user_input == "paper" and ai_input == "rock":
        print("You win!")
        user_wins +=1
    
    elif user_input == "scissors" and ai_input == "paper":
        print("You win!")
        user_wins +=1

    elif user_input == ai_input:
        print("It's a draw! Nobody wins this round.")
        draws +=1

    else:
        print("You lose!")
        ai_wins +=1

print(f"You won {user_wins} times. The AI won {ai_wins} times. You drew {draws} times.")
