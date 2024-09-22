def main():
    '''
        Loads the game data loops until either the game is complete as expected.
    '''
    game_data = load_game_data()
    keep_going = True
    current_node_key = "start"

    # continuiously loop until the game is completed as expected.
    while keep_going:
        # get the next node key from the user
        current_node_key = get_next_node(current_node_key, game_data)

        # is the game complete
        if current_node_key == "quit":
            keep_going = False
            continue

def load_game_data():
    '''
        Loads the game data.

        returns:
            Dictionary of the game data to use
    '''

    # load the game data and returns a dictionary of the game data.
    game_data =  {
        "start": ["You stand at the entrance of a dark forest. The path splits into two.", "Enter the forest", "forest", "Follow the river", "river"], 
        "forest": ["The forest is dense and eerie. You hear rustling in the bushes.", "Investigate the noise", "noise", "Continue deeper into the forest", "deep"], 
        "river": ["The river flows swiftly. You see a boat tied to a tree.", "Take the boat", "boat", "Walk along the riverbank", "bank"], 
        "noise": ["A rabid squirrel jumps out and attacks you.  You do not make it.", "Start over", "start", "Quit", "quit"], 
        "deep": ["You find a hidden cave with glowing crystals.", "Enter the cave", "cave", "Turn back", "start"], 
        "boat": ["The boat takes you to a small island with a treasure chest.", "Open the chest", "chest", "Return to the shore", "river"], 
        "bank": ["You find a bridge leading to a village.", "Cross the bridge", "village", "Return to the forest", "forest"], 
        "cave": ["The cave is filled with ancient artifacts.", "Examine the artifacts", "artifacts", "Leave the cave", "deep"], 
        "chest": ["The chest is filled with gold and jewels. You are rich!", "Start over", "start", "Quit", "quit"], 
        "village": ["The villagers welcome you and offer you a place to stay.", "Start over", "start", "Quit", "quit"], 
        "artifacts": ["You accidentally trigger a trap and the cave collapses.", "Start over", "start", "Quit", "quit"], 
    }

    # return the loaded game data.
    return game_data

def get_next_node(current_node_key, game_data):
    '''
        Takes the game data passed in and displays the description, and both
        options to the end user.

        returns:
            String of the selected option's key
    '''

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

main()