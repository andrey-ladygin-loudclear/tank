
import random

import pyglet
from cocos import sprite
from cocos.actions import Action

from helpers import Global
from objects.Bullet import Bullet
from objects.animations.ExplosionStandartBulletAnimation import explosionStandartBulletAnimation


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
        Global.GameLayers.removeAnimation(self)
        # if self in Global.layers['bullets']: Global.layers['bullets'].remove(self)
        # if self in Global.objects['bullets']: Global.objects['bullets'].remove(self)

    def destroy(self, position=None):
        super(StandartBullet, self).destroy()
        animation = explosionStandartBulletAnimation()
        animation.appendAnimationToLayer(position, self.rotation)