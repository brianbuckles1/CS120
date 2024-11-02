import simpleGE, random

class Mineral(simpleGE.Sprite):
    """
    Mineral
    inherits simpleGE.Sprite
    Base class used for different minerals in the game
    """
    def __init__(self, scene, image):
        """
        Mineral base initialization method
        :param scene: scene the sprite is one
        :param image: image to use for the sprite
        """
        super().__init__(scene)

        self.setImage(image)
        self.setSize(50, 50)
        self.minSpeed = 1
        self.maxSpeed = 8

        self.reset()

    def checkBounds(self):
        """
        check the sprite is at the bottom and reset if it is
        :return: void
        """
        if self.bottom > self.screenHeight:
            self.reset()

    def reset(self):
        self.position = (random.randint(50, self.screenWidth), 100)
        self.dy = random.randint(1, 8)


class Gem(Mineral):
    """
    Gem
    Inherits Mineral which inherits from simpleGE.Sprite
    Creates a gem sprite to be used by the scene.
    """
    def __init__(self, scene):
        """
        initializes the Gem sprite class and set the sprite image and movement
        :param scene:
        """
        super().__init__(scene, "assets/gem.png")

class Rock(Mineral):
    """
    Gem
    Inherits Mineral which inherits from simpleGE.Sprite
    Creates a rock sprite to be used by the scene.
    """
    def __init__(self, scene):
        """
        initializes the Rock sprite class and set the sprite image and movement
        :param scene:
        """
        super().__init__(scene, "assets/rock.png")
