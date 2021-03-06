import math

import cocos.collision_model as cm

from components.NetworkCodes import NetworkActions, NetworkDataCodes


class LandingObject():
    id = 0
    health = 80
    position = (0, 0)

    width = 32
    height = 32
    scale = 1

    type = 0
    src = ''

    def __init__(self, obj):
        self.type = obj.get('type')
        self.src = obj.get('src')
        self.set_position(obj.get('position'))

    def damage(self, bullet):
        x, y = self.position
        x2, y2 = bullet.position
        deltax = math.pow(x - x2, 2)
        deltay = math.pow(y - y2, 2)
        delta = (deltax + deltay) / 3
        range = math.sqrt(max(delta / self.width, 1))
        self.health -= bullet.damage / range

    # def destroy(self):
    #     Global.Queue.append({
    #         "action": Global.NetworkActions.DESTROY,
    #         Global.NetworkDataCodes.TYPE: Global.NetworkDataCodes.WALL,
    #         Global.NetworkDataCodes.POSITION: self.position,
    #         Global.NetworkDataCodes.ID: self.id
    #     })
    #
    #     if self in Global.GameObjects.getWalls(): Global.GameObjects.removeWall(self)


    def getPoints(self):
        x, y = self.position
        w, h = (self.width * self.scale, self.height * self.scale)
        x1, y1 = x - w / 2, y - h / 2
        x2, y2 = x + w / 2, y - h / 2
        x3, y3 = x + w / 2, y + h / 2
        x4, y4 = x - w / 2, y + h / 2

        return ((x1, y1),(x2, y2),(x3, y3),(x4, y4))

    def set_position(self, pos):
        self.position = pos
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def getObjectFromSelf(self):
        return {
            'action': NetworkActions.UPDATE,
            NetworkDataCodes.ID: self.id,
            NetworkDataCodes.POSITION: self.position,
            NetworkDataCodes.TYPE: self.type,
            NetworkDataCodes.SCALE: self.scale,
            NetworkDataCodes.SRC: self.src
        }