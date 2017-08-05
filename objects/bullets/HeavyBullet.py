
import random

import pyglet

from cocos import sprite
from cocos.actions import Action

from helpers import Global
from objects.Bullet import Bullet
from objects.animations.ExplosionHeavyBulletAnimation import explosionHeavyBulletAnimation
from objects.animations.ExplosionStandartBulletAnimation import explosionStandartBulletAnimation


class HeavyBullet(Bullet):
    type = 'HeavyBullet'
    spriteName = 'assets/bullets/bullet-origin.png'
    startPosition = (0, 0)

    scale = 1
    damage = 10
    damageRadius = 20
    velocity = (0, 0)
    fireLength = 1000

    speed = 600

    def __init__(self):
        super(HeavyBullet, self).__init__(self.spriteName)

    def removeAnimation(self):
        Global.GameLayers.removeAnimation(self)

    def destroy(self, position=None):
        super(HeavyBullet, self).destroy()
        animation = explosionHeavyBulletAnimation()
        animation.appendAnimationToLayer(position, self.rotation)
