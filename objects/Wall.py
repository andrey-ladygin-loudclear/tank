import math
from cocos import sprite
import cocos.collision_model as cm

from helpers import Global
from helpers.HealthHelper import HealthHelper


class Wall(sprite.Sprite):
    health = 20
    id = 0

    healthHelper = None

    def __init__(self, sprite, type):
        super(Wall, self).__init__(sprite)

        if type == 5:
            self.healthHelper = HealthHelper(self)

    def update_position(self, position):
        self.position = position
        if self.healthHelper: self.healthHelper.updateHealthPosition()
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def damage(self, bullet):
        x, y = self.position
        x2, y2 = bullet.position
        deltax = math.pow(x - x2, 2)
        deltay = math.pow(y - y2, 2)
        delta = (deltax + deltay) / 3
        range = math.sqrt(max(delta / self.width, 1))
        #print('range: ' + str(range))
        #print('damage: ' + str(bullet.damage * bullet.damage / range ))
        self.health -= bullet.damage / range

    def destroy(self):
        if self in Global.GameObjects.getWalls(): Global.GameObjects.removeWall(self)
        self.healthHelper.destroy()