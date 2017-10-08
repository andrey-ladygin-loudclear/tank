import random

import math
from time import time

from components import Global
from movingHandlers.BulletMovingHandlers import BulletMovingHandlers
from objects.animations.HeavyBulletFireAnimation import HeavyBulletFireAnimation
from objects.animations.StandartBulletFireAnimation import StandartBulletFireAnimation
from objects.bullets.StandartBullet import StandartBullet


class MiniGunWeapon:
    def getAngleDeflection(self):
        return random.randrange(-500, 500) / 100

    def fire(self, id=None, position=None, animation_position=None, rotation=None, animation_rotation=None, last_update_time=None, parent_id=None):
        bullet = StandartBullet()

        # if not position: position = self.firePosition()
        # if not rotation: rotation = self.fireRotation()
        if not last_update_time: last_update_time = time()

        bullet.id = id
        bullet.parent_id = parent_id
        bullet.position = position
        bullet.start_position = position
        bullet.rotation = rotation
        bullet.last_update_time = last_update_time

        Global.addBulletToGame(bullet)
        bullet.do(BulletMovingHandlers())

        animation = StandartBulletFireAnimation()
        animation.appendAnimationToLayer(animation_position, animation_rotation)