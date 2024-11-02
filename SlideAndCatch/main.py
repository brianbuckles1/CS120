import scenes.game

def main():
    keepGoing = True
    bestScore = 0
    game = scenes.game.Game((800,600))

    while keepGoing:
        game.start()


main()