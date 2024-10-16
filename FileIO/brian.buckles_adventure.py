import json

DEFAULT_GAME_FILE="default.data"
SAVED_GAME_FILE="saved.data"

def main():
    keep_going = True
    game_data = loadGame(DEFAULT_GAME_FILE)
    menu = getMenu()

    while(keep_going):
        user_menu_choice = getMenuChoice(menu)

        match user_menu_choice:
            case 0:
                keep_going = False
            case 1:
                game_data = loadGame(DEFAULT_GAME_FILE)
            case 2:
                game_data = loadGame(SAVED_GAME_FILE)
            case 3:
                saveGame(game_data,SAVED_GAME_FILE)
            case 4:
                editNode(game_data)
            case 5:
                playGame(game_data)

def getMenu():
    menu = [
        "Exit the game",
        "Load default game",
        "Load saved game",
        "Save game",
        "Add or Edit a node",
        "Play game"
    ]

    return menu

def getMenuChoice(menu):
    keep_going = True
    user_menu_choice = 0

    while(keep_going):
        print("\nPlease choose from the following options:")
        for index, menuItem in enumerate(menu):
            print(f'{index}.) {menuItem}')
        
        user_menu_choice = input("Please select from the numbers above: ")
        if user_menu_choice.isnumeric() and int(user_menu_choice) < len(menu):
            keep_going = False

    return int(user_menu_choice)

def playGame(game_data):
    '''
        plays the game data loops until either the game is complete as expected.
    '''
    keep_going = True
    current_node_key = "start"

    # continuiously loop until the game is completed as expected.
    while keep_going:
        # get the next node key from the user
        current_node_key = playNode(current_node_key, game_data)

        # is the game complete
        if current_node_key == "quit":
            keep_going = False
            continue

def playNode(current_node_key, game_data):
    '''
        Takes the game data passed in and displays the description, and both
        options to the end user.

        returns:
            String of the selected option's key
    '''

    print(current_node_key)
    # set the current node
    current_node = game_data[current_node_key]

    # print out the description from the current node
    print(f'\n{current_node[0]}')
 
    # print out the options the user can choose from
    print(f'\t1.) {current_node[1]}')
    print(f'\t2.) {current_node[3]}\n')

    # get and hold the users choice
    user_choice = input("choose your next path (1 or 2): ")

    # validate the user's choice is a 1 or a 2 only
    if user_choice not in ("1","2"):
        print("invalid choice! you must choose a 1 or a 2 please.")
        return current_node_key
    
    # return the selected options node to move to next
    return current_node[int(user_choice) * 2]

def editNode(game_data):
    print("\nNodes:")
    for node in game_data:
        # print node name
        print(f'\t{node}')
    
    user_node_choice = input("Please type the node name you wish to edit: ")
    current_node_data = [None]*5
    updated_node_data = []

    if user_node_choice in game_data:
        current_node_data = game_data[user_node_choice]

    print(current_node_data[0])

    updated_node_data.append(editField(f"Description ({current_node_data[0]}): ", current_node_data[0]))
    updated_node_data.append(editField(f"Menu A ({current_node_data[1]}): ", current_node_data[1]))
    updated_node_data.append(editField(f"Node A ({current_node_data[2]}): ", current_node_data[2]))
    updated_node_data.append(editField(f"Menu B ({current_node_data[3]}): ", current_node_data[3]))
    updated_node_data.append(editField(f"Node B ({current_node_data[4]}): ", current_node_data[4]))

    # update or create node
    game_data[user_node_choice] = updated_node_data

    return game_data

def editField(text, current_value):
    val = input(text)
    if val.strip() == "":
        return current_value
    
    return val

def saveGame(game_data, file_name):
    with open(file_name,"w") as file:
        json.dump(game_data, file, indent=2)

def loadGame(file_name):
    game_data = {}
    with open(file_name, "r") as file:
        game_data = json.load(file)

    return game_data

main()
