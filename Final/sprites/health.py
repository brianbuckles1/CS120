import simpleGE

class Health(simpleGE.Sprite):
    def __init__(self, scene:simpleGE.Scene, position=(50, 700)):
        super().__init__(scene)
        self.setImage("assets/heart.png")
        self.setSize(50, 50)
        self.position = position