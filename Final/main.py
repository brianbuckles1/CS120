import json

import scenes.game, scenes.menu

def main():
    keepGoing = True
    high_score = 0

    # load persistent data from save file
    savedData = loadData()
    if savedData:
        high_score = int(savedData["high_score"])

    while keepGoing:
        # start the main menu
        main_menu = scenes.menu.MainMenu((800, 400), high_score)
        main_menu.start()

        if main_menu.get_command() == "play":
            # start the game
            game = scenes.game.Game()
            game.start()

            # check if the score is higher than the high score
            if game.get_score() > high_score:
                high_score = game.get_score()
                saveData(high_score)

        # check if the user wants to quit
        elif main_menu.get_command() == "quit":
            keepGoing = False

def loadData():
    """
    Load the save file
    """
    # create a default save data
    saveData = []

    try:
        # load the save file
        with open("save.dat", "r") as file:
            saveData = json.load(file)
            print(f"Save file loaded {saveData}")
    # if the file is not found print an error message stating such
    except FileNotFoundError as e:
        print("No save file found")
    # if there is an error loading the file print an error message
    except IOError as e:
        print(f"Error loading JSON: {str(e)}")
    return saveData

def saveData(high_score:int):
    """
    Save the high score
    """
    saveData = {
        "high_score": high_score
    }

    try:
        # save the high score to the save file
        with open("save.dat", "w") as file:
            json.dump(saveData, file)
    # if there is an error saving the file print an error message
    except IOError as e:
        print(f"Error saving JSON: {str(e)}")

if __name__ == "__main__":
    main()