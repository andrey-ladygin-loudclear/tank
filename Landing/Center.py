from Landing.Building import Building
import cocos.collision_model as cm


class Center(Building):
    health = 1000
    maxHealth = 1000
    src = 'assets/buildings/center.png'

    def __init__(self, id=0, position=(0,0), rotation=0, clan=1):
        super(Center, self).__init__(id=id, position=position, rotation=rotation, clan=clan)

        self.scale = 0.7
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )