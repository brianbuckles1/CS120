import simpleGE

class MainMenu(simpleGE.Scene):
    """
    MainMenu class
    handles create the game sprites and sounds and handling collisions
    """
    def __init__(self, size=(800,400), high_score:int=0):
        """
                Game initialization method
                :param size: tuple of dimensions. Defaults 800 x 600
                """
        super().__init__(size)

        self.sprites = []
        self.__command = 'play'
        self.__high_score = high_score

        # create the title
        lbl_title = simpleGE.Label()
        lbl_title.text="Gladiator"
        # lbl_title.set_font_size(50)
        lbl_title.size= (400,60)
        lbl_title.fgColor = "white"
        lbl_title.center = (200, 40)
        lbl_title.clearBack = True
        self.sprites.append(lbl_title)

        # create label for high score
        lbl_high_score = simpleGE.Label()
        lbl_high_score.text = f"High Score: {self.__high_score}"
        lbl_high_score.center = (600,25)
        lbl_high_score.fgColor="white"
        self.sprites.append(lbl_high_score)

        # create multi label for instructions
        mlbl_instructions = simpleGE.MultiLabel()
        mlbl_instructions.size = (550, 250)
        mlbl_instructions.textLines = [
            "Instructions:"
            ,""
            ,"Fight off as many gladiators as you can."
            ,""
            ,"You start the game with 3 lives and each time you"
            ,"get hit, you will lose 1 life. The game is over when"
            ,"you have no lives remaining."
        ]
        mlbl_instructions.bgColor = "black"
        mlbl_instructions.fgColor = "white"
        mlbl_instructions.center = (500, 250)

        self.sprites.append(mlbl_instructions)

        # create button for starting the game
        self.btn_play = simpleGE.Button()
        self.btn_play.text = "Play"
        self.btn_play.center = (100,150)
        self.sprites.append(self.btn_play)

        # create button for exiting the game
        self.btn_quit = simpleGE.Button()
        self.btn_quit.text = "Quit"
        self.btn_quit.center = (100,200)
        self.sprites.append(self.btn_quit)

    def process(self):
        """
        process the current frame
        :return:
        """
        if self.btn_quit.clicked:
            self.__command = "quit"
            self.stop()
        if self.btn_play.clicked:
            self.__command = "play"
            self.stop()

    def get_command(self)->str:
        """
        get the command of the button pressed
        :return: string command
        """
        return self.__command

    def set_high_score(self, high_score:int = 0):
        """
        set the high score for the menu
        :param high_score: integer of the score to display as the high score
        :return:
        """
        self.__high_score = high_score


if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.start()
    print(main_menu.get_command())
    print("done")