from cocos import sprite


class Tower(sprite.Sprite):
    id = 0
    health = 1000
    type = 5

    src = 'assets/towers/heavy-murder-final-turret-v2.png'

    def __init__(self, position=(0,0)):
        super(Tower, self).__init__(self.src)
        self.position = position
