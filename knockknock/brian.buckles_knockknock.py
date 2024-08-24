# Mad Lib Game
# Brian Buckles
# 8/18/2024

# variables and inputs
user_name = input("What is your name? ")
user_play = input(f"Hi {user_name}, Would you like to hear a knock knock joke? ")[0]

# check if we need to continue the game
if user_play.casefold() != "y".casefold():
    print("Awe man I had a really good one for you.")
    exit()

print("Knock, Knock")

# get user response
user_whos_there = input("Your turn: ")

# check response
if user_whos_there.casefold() != "who's there?".casefold():
    print("Sorry, I was expecting 'Who's there?'")
    exit()

joke_name = "Radio"
print(joke_name)

user_who = input("Your turn: ")
# check response matches concatination of joke_name + ' who?'
if user_who.casefold() != f"{joke_name} who?".casefold():
    print(f"Sorry, I was expecting you to say '{joke_name} who?'")
    exit()

# output the final result to the user.
print("Radio not, here I come!")
print("That was fun!  Thank you for playing along!")