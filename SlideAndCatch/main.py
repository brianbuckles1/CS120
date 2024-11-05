import scenes.game, scenes.menu

def main():
    keepGoing = True
    high_score = 0

    while keepGoing:
        main_menu = scenes.menu.MainMenu((800, 400), high_score)
        main_menu.start()

        if main_menu.get_command() == "play":
            game = scenes.game.Game((800,600))
            game.start()

            if game.get_score() > high_score:
                print("setting new high score")
                high_score = game.get_score()
                print(high_score)
        elif main_menu.get_command() == "quit":
            keepGoing = False



if __name__ == "__main__":
    main()