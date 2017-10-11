from threading import Timer

import math
from cocos import sprite

from components import Global, NetworkCodes
from components.NetworkCodes import NetworkActions, NetworkDataCodes
from helpers.DamageHelper import DamageHelper
from helpers.HealthHelper import HealthSprite
from objects.weapons.MiniGunWeapon import MiniGunWeapon
import cocos.collision_model as cm


class Building(sprite.Sprite):
    id = 0

    health = 100.0
    maxHealth = 100.0

    type = 0

    clan = 1
    src = ''

    healthHelper = True

    def __init__(self, id=0, position=(0,0), rotation=0, clan=1):
        super(Building, self).__init__(self.src)
        if not id: id = Global.getNextId()

        self.id = id
        self.position = position
        self.rotation = rotation
        self.clan = clan

        self.healthHelper = HealthSprite()
        self.updateHealthPosition()

        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def damage(self, bullet):
        dx = (self.width + self.height) * self.scale / 2
        dmg = DamageHelper.get_damage(self.position, bullet, dx)

        self.health -= dmg

        Global.damageSomeObject(id=self.id, dmg=dmg, health=self.health)

        Global.Queue.append({
            "action": NetworkActions.DAMAGE,
            NetworkDataCodes.TYPE: NetworkDataCodes.TANK,
            NetworkDataCodes.TANK_ID: self.id,
            NetworkDataCodes.HEALTH: self.health,
            NetworkDataCodes.DAMAGE: dmg
        })

    def destroy(self):
        raise('You should add Destroy method in MiniGunTower')

    def getObjectFromSelf(self):
        x, y = self.position
        r = self.rotation

        return {
            'action': NetworkCodes.NetworkActions.UPDATE,
            NetworkCodes.NetworkDataCodes.OBJECT_ID: self.id,
            NetworkCodes.NetworkDataCodes.POSITION: (int(x), int(y)),
            NetworkCodes.NetworkDataCodes.ROTATION: int(r),
            NetworkCodes.NetworkDataCodes.CLAN: self.clan,
            NetworkCodes.NetworkDataCodes.HEALTH: self.health,
        }

    def updateHealthPosition(self):
        if self.healthHelper: self.healthHelper.updateHealthPosition(self.position)

    def setHealth(self, health):
        self.healthHelper.setHealth(int(float(health)/self.maxHealth * 100))