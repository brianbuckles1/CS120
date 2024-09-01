import random

# all fortune outcomes
fortunes = ("Possibly", " Very Likely", "Probably Not", "You have a good possibility", "Not Likely", "Uncertain", "Yes", "No"," Vote is still out")

# menu items
menu_items = ("1.) Show All Fortunes", "2.) Show Specific Fortune", "3.) Ask Your Question")
print("1 Show all Fortunes")
print("2 Show Specific Fortune")
print("3 Ask your question for your fortune")

# set the menu selection from the user input
menu_selection = input("What is your numberic selection: ")

# if menu selection is 1 print out fortunes
if menu_selection[0] == "1":
    # loop and print out the fortunes
    for (index,fortune) in enumerate(fortunes):
        print(f"{index} - {fortune}")
    # exit
    exit()

# if menu selection is 2 we need to get the index for the fortune the user would like to see.
if menu_selection[0] == "2":
    specific_fortune = input(f"What is the index for fortune would you like to see? 0 - {len(fortunes) - 1}: ")

    # check if specific fortune is numeric
    if not specific_fortune.isnumeric():
        print(f"Well that is not what I was looking for. I needed a number.")

    # convert to integer
    fortune_index = int(specific_fortune)

    # validate fortune_index is in range of fortune indexes.
    if not fortune_index in range(0, len(fortunes)):
        print("well that is not a valid index")
        exit();

    print(f"{fortunes[fortune_index]}")
    exit()

# if menu selection is 3 we need to get the user question and generate the response.
if menu_selection[0] == "3":
    # get users question
    question = input("What question would you like to ask: ")
    # display the question back to the user.
    print(f"Your Question: {question}")
    # generate the random integer for the fortunes index range
    random_int = random.randint(0, len(fortunes)-1)
    # print out the fortune for the random_int
    print(f"{fortunes[random_int]}")
    exit()

print("shucks, well you didn't follow my directions and put in a valid menu selection.")
