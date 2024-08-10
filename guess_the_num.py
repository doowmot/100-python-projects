import random

username = input('want to play a game...? what is your name? ')

print('well, ' + username + ', were going to have some fun...')
print('i am thinking of a number between 1 and 10. What is the number?')

secretNumber = random.randint(1, 10)

for numGuesses in range(1-6):
    guess = int(input())

    if guess < secretNumber:
        print('wrong. too low. try again.')
    elif guess > secretNumber:
        print('wrong. too high. try again.')
    else:
        break

    if guess == secretNumber:
        print('you have beaten my this time ' + username + '. well done. it took you ' + str(numGuesses) + ' guesses')
    else:
        print('haha. you are rubbish ' + username + '. the number i was thinking of is ' + str(secretNumber))


