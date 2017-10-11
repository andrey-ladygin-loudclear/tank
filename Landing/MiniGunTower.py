from threading import Timer

import math
from cocos import sprite

from Landing.Building import Building
from components import Global, NetworkCodes
from components.NetworkCodes import NetworkActions, NetworkDataCodes
from helpers.DamageHelper import DamageHelper
from helpers.HealthHelper import HealthSprite
from objects.weapons.MiniGunWeapon import MiniGunWeapon
import cocos.collision_model as cm


class MiniGunTower(Building):
    health = 1000.0
    maxHealth = 1000.0

    src = 'assets/towers/heavy-murder-final-turret-v2.png'

    weapon = None
    canFire = True
    bulletFreezTime = 0.1

    def __init__(self, id=0, position=(0,0), rotation=0, clan=1):
        super(MiniGunTower, self).__init__(id=id, position=position, rotation=rotation, clan=clan)
        self.weapon = MiniGunWeapon()
        self.scale = 0.3
        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def getFirePosition(self, dx, dy):
        cos_x = math.cos(math.radians(self.rotation - 180))
        sin_x = math.sin(math.radians(self.rotation))
        x = self.x + dx * sin_x + dy * cos_x
        y = self.y - dx * cos_x + dy * sin_x
        return (x, y)

    def fire(self):
        if not self.canFire: return

        id = Global.getNextId()
        rotation = self.rotation - 90
        animation_rotation = self.rotation
        parent_id = self.id

        animation_position = self.getFirePosition(-30, -10)
        position = self.getFirePosition(-30, -10)

        self.weapon.fire(id=id, position=position, animation_position=animation_position,
                         animation_rotation=animation_rotation, rotation=rotation, parent_id=parent_id)
        self.canFire = False
        Timer(self.bulletFreezTime, self.acceptFire).start()

    def acceptFire(self):
        self.canFire = True