import simpleGE

class Health(simpleGE.Sprite):
    """
    Health class
    """
    def __init__(self, scene:simpleGE.Scene, position=(50, 700)):
        """
        Initialize the Health sprite
        """
        super().__init__(scene)

        # set the image assets
        self.setImage("assets/heart.png")

        # set the size of the sprite
        self.setSize(50, 50)

        # set the position of the sprite
        self.position = position