import math
import random
from threading import Timer

from cocos import sprite

from objects.weapons.HeavyWeapon import HeavyWeapon
from objects.weapons.LightWeapon import LightWeapon


class Gun(sprite.Sprite):
    weapon1 = None
    weapon2 = None

    canFire = True
    canHeavyFire = True

    bulletFreezTime = 0.15
    heavyBulletFreezTime = 1

    tank = None

    def __init__(self, spriteName, tank):
        super(Gun, self).__init__(spriteName)
        self.image_anchor = (self.image.width / 2, self.image.height / 2 + 20)
        self.weapon1 = HeavyWeapon(self)
        self.weapon2 = LightWeapon(self)
        self.tank = tank

    def fireFirstWeapon(self):
        if self.canHeavyFire:
            self.weapon1.fire()
            self.canHeavyFire = False
            Timer(self.heavyBulletFreezTime, self.acceptHeabyFire).start()

    def fireSecondWeapon(self):
        if self.canFire:
            self.weapon2.fire()
            self.canFire = False
            Timer(self.bulletFreezTime, self.acceptFire).start()

    def getRotation(self):
        return self.rotation

    def acceptFire(self): self.canFire = True
    def acceptHeabyFire(self): self.canHeavyFire = True