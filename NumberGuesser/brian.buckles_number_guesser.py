import random

# number of guesses we want the user to have
number_of_guesses = 0
# number we want the user to guess in order to win
winning_number = random.randint(0,100)
# keep going boolean to control the while loop for the game
keep_going = True

print("Number Guesser")
print("You have 7 guesses to guess my number")

# loop while keep_going is true
while keep_going:
    if number_of_guesses >= 7:
        print("Aww man you ran out of guesses.")
        keep_going=False
        continue

    # get the users guess input
    user_guess = input(f"{number_of_guesses + 1}) What is your guess? ")

    # check if valid number
    if not user_guess.isnumeric():
        print("Sorry that is not a number and it cost you a guess.")
        # add 1 to the guess
        number_of_guesses += 1
        # exit out of this iteration
        continue

    # convert user_guess to integer
    user_guess_number = int(user_guess)

    # check if it is the winning number
    if user_guess_number == winning_number:
        print("Congrats, you have won!")
        keep_going = False
        continue

    # check if it is less than the winning number and let the user know
    if user_guess_number < winning_number:
        print("Your guess is too low")

    # check if it is greater than the winning number and let the user know
    if user_guess_number > winning_number:
        print("Your guess is too high")

    # add 1 to the number of guesses
    number_of_guesses += 1

# The loop ended thank the user for playing.
print("Thank you for playing!")


