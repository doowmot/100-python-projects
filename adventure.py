user_name = input("Welcome weary adventurer. May I take your name? ")
print(f"Well, {user_name}, it's great to mee you.")

answer = input(f"Ok {user_name}, you stumble across a distinguished gentleman. A glistening, gold watch, well-suited, with a tie stangling his middle-aged neck. Do you say 'hello' or 'ignore him'? ")

if answer == "hello":
    answer = input("The gentleman extends his hand and gives yours a firm shake. The overpriced cologne instantly invades your nostrils. He invites you back to his place. Do you want to 'follow' or 'not'? ")
    if answer == "follow":
        print("You arrive at his contemporary, minimalist apartment. He instantly bludgeons you with a well-worn baseball bat. Your skull cracks into a thousand pieces. You're dead. Game over.")
        exit()
    elif answer == "not":
        print("noice.")

elif answer == "ignore him":
    print("The gentleman continues to stare soullessly into his iPhone, checking his stock trading portfolio with a mix of hope and greed.")
else:
    print("Invalid input. The adventure ends here.")
