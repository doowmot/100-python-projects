import random

random_num = random.randint(1, 10)
counter = 1

while True:

    guess = int(input("I'm thinking of a number between 1 and 10. What is the number? "))

    if guess < random_num:
        print('wrong. too low. try again.')
        counter += 1
    elif guess > random_num:
        print('wrong. too high. try again.')
        counter +=1
    elif guess == random_num:
        print(f"Well done. it took you {counter} guesses")
    else:
        break


