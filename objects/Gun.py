import math
import random

from cocos import sprite

from objects.weapons.HeavyWeapon import HeavyWeapon
from objects.weapons.LightWeapon import LightWeapon


class Gun(sprite.Sprite):

    weapon1 = None
    weapon2 = None

    canFire = True
    canHeavyFire = True

    tank = None

    def __init__(self, spriteName, tank):
        super(Gun, self).__init__(spriteName)
        self.image_anchor = (self.image.width / 2, self.image.height / 2 + 20)
        self.weapon1 = HeavyWeapon(self)
        self.weapon2 = LightWeapon(self)
        self.tank = tank

    def fireFirstWeapon(self):
        self.weapon1.fire()

    def fireSecondWeapon(self):
        self.weapon2.fire()

    def getRotation(self):
        return self.rotation