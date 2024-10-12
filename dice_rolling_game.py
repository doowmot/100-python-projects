import random

counter = 0
total = 0

while True:
    choice = input("Roll the dice? (y/n) ").lower()
    if choice == "y":
        try: 
            num_dice = int(input("How many dice would you like to roll? "))
            counter += num_dice
            roll_sum = 0
            for i in range(num_dice):
                roll = random.randint(1, 6)
                print(f"Dice {i+1} = {roll}")
                roll_sum += roll
            total += roll_sum
            print(f"You have rolled {counter} dice in total and they've added up to {total}")
        except:
            print("Enter a valid option")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")