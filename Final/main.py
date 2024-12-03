import json

import scenes.game, scenes.menu

def main():
    keepGoing = True
    high_score = 0

    saveData = loadSave()
    if saveData != []:
        high_score = int(saveData["high_score"])

    while keepGoing:
        main_menu = scenes.menu.MainMenu((800, 400), high_score)
        main_menu.start()

        if main_menu.get_command() == "play":
            game = scenes.game.Game()
            game.start()

            if game.get_score() > high_score:
                high_score = game.get_score()
                save(high_score)
        elif main_menu.get_command() == "quit":
            keepGoing = False

def loadSave():
    """
    Load the save file
    """
    saveData = []

    try:
        with open("save.dat", "r") as file:
            saveData = json.load(file, encoding="utf-8")
            print(f"Save file loaded {saveData}")
    except FileNotFoundError:
        print("No save file found")

    return saveData

def save(high_score:int):
    """
    Save the high score
    """
    saveFile = {
        "high_score": high_score
    }
    with open("save.dat", "w") as file:
        json.dump(saveFile, file)

if __name__ == "__main__":
    main()