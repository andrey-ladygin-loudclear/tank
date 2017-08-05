import random

import math
from time import time

from helpers import Global
from movingHandlers.BulletMovingHandlers import BulletMovingHandlers
from objects.animations.HeavyBulletFireAnimation import HeavyBulletFireAnimation
from objects.bullets.HeavyBullet import HeavyBullet


class HeavyWeapon:
    heavy_fire_offset_x = -20
    heavy_fire_offset_y = 0
    heavy_fire_animation_offset_x = -35
    heavy_fire_animation_offset_y = 0

    gun = None

    def __init__(self, gun):
        self.gun = gun

    def getAngleDeflection(self):
        return random.randrange(-200, 200) / 100

    def firePosition(self):
        cos_x = math.cos(math.radians(self.gun.rotation - 180))
        sin_x = math.sin(math.radians(self.gun.rotation))
        x = self.gun.x + self.heavy_fire_offset_x * sin_x + self.heavy_fire_offset_y * cos_x
        y = self.gun.y - self.heavy_fire_offset_x * cos_x + self.heavy_fire_offset_y * sin_x
        return (x, y)

    def fireRotation(self):
        return self.gun.rotation - 90 + self.getAngleDeflection()

    def fireAnimationPosition(self):
        cos_x = math.cos(math.radians(self.gun.rotation - 180))
        sin_x = math.sin(math.radians(self.gun.rotation))
        x = self.gun.x + self.heavy_fire_offset_x * sin_x + self.heavy_fire_offset_y * cos_x
        y = self.gun.y - self.heavy_fire_offset_x * cos_x + self.heavy_fire_offset_y * sin_x
        anim_x = x + self.heavy_fire_animation_offset_x * sin_x + self.heavy_fire_animation_offset_y * cos_x
        anim_y = y - self.heavy_fire_animation_offset_x * cos_x + self.heavy_fire_animation_offset_y * sin_x
        return (anim_x, anim_y)

    def fire(self, id=None, position=None, rotation=None, last_update_time=None):
        bullet = HeavyBullet()

        if not position: position = self.firePosition()
        if not rotation: rotation = self.fireRotation
        if not last_update_time: last_update_time = time()

        bullet.id = id
        bullet.parent_id = self.gun.tank.id
        bullet.position = position
        bullet.start_position = position
        bullet.rotation = rotation
        bullet.last_update_time = last_update_time

        Global.GameObjects.addBullet(bullet)
        bullet.do(BulletMovingHandlers())

        animation = HeavyBulletFireAnimation()
        animatiom_position = self.fireAnimationPosition()
        animation.appendAnimationToLayer(animatiom_position, self.gun.rotation)