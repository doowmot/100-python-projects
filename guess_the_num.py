import random

def play_game():
    lower_range = int(input("Lowest possible number: "))
    higher_range = int(input("Highest possible number: "))
    random_num = random.randint(lower_range, higher_range)
    num_user_guesses = int(input("Number of guesses allowed: "))
    
    counter = 0
    while num_user_guesses > 0:
        guess = int(input(f"Guess the number ({num_user_guesses} guesses left): "))
        counter += 1
        num_user_guesses -= 1
        
        if guess == random_num:
            return counter
        elif guess < random_num:
            print("Too low!")
        else:
            print("Too high!")
    
    print(f"Game over. The answer was {random_num}.")
    return None

best_score = float('inf')
while True:
    result = play_game()
    if result:
        print(f"Well done! It took you {result} guesses.")
        best_score = min(best_score, result)
    print(f"Your best score is {best_score}")
    
    if input("Play again? (y/n): ").lower() != 'y':
        break

print("Thanks for playing!")