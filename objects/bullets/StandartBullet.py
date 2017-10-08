import pyglet

from components import Global
from objects.Bullet import Bullet
from objects.animations.ExplosionStandartBulletAnimation import explosionStandartBulletAnimation
from objects.animations.ExplosionStandartBulletAnimation2 import explosionStandartBulletAnimation2
from objects.animations.StandartBulletFireAnimation import StandartBulletFireAnimation


class StandartBullet(Bullet):
    type = 'StandartBullet'
    spriteName = 'assets/bullets/bullet.png'
    startPosition = (0, 0)

    scale = 0.8
    damage = 1
    damageRadius = 5
    velocity = (0, 0)
    fireLength = 1000

    speed = 400

    def __init__(self):
        super(StandartBullet, self).__init__(self.spriteName)

    def removeAnimation(self):
        Global.Layers.removeAnimation(self)
        # if self in Global.layers['bullets']: Global.layers['bullets'].remove(self)
        # if self in Global.objects['bullets']: Global.objects['bullets'].remove(self)

    def destroy(self, position=None):
        super(StandartBullet, self).destroy()
        return
        #animation = explosionStandartBulletAnimation()
        #animation.appendAnimationToLayer(position, self.rotation)
        #animation.appendAnimationToLayer(position)
        #super(StandartBullet, self).destroy()