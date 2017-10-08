import random

import cocos
import cocos.collision_model as cm
import math
from cocos import sprite
from cocos.layer import ColorLayer

from components import NetworkCodes, Global
from components.NetworkCodes import NetworkActions, NetworkDataCodes
from helpers.HealthHelper import HealthSprite
from objects.Gun import Gun
from objects.animations.ExplosionTankAnimation import ExplosionTankAnimation
from objects.animations.HeavyBulletFireAnimation import HeavyBulletFireAnimation


class Tank(sprite.Sprite):
    Gun = None
    gun_rotation = 0
    id = 0
    type = 1

    speed = 30
    health = 100

    old_position = (0, 0)
    velocity = (0, 0)

    maxBulletsHolder = 10
    bulletsHolder = 10
    timeForBulletsHolderReload = 3

    healthHelper = None

    spriteName = 'assets/tank/parts/E-100_1.png'
    spriteGunName = 'assets/tank/parts/E-100_2.png'

    bot = False
    clan = 0
    rotation_speed = 1
    gun_rotation_speed = 1
    speed_acceleration = 1
    max_speed = 20


    def __init__(self):
        self.Gun = Gun(self.spriteGunName, self)
        super(Tank, self).__init__(self.spriteName)
        self.scale = self.Gun.scale = 0.5

        self.healthHelper = HealthSprite()
        self.updateHealthPosition()

        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def _update_position(self):
        super(Tank, self)._update_position()
        self.Gun.position = self.position
        self.Gun.rotation = self.rotation + self.gun_rotation

        self.updateHealthPosition()

        # self.rotation = 180
        # self.Gun.position = self.position
        # self.Gun.rotation = self.rotation + self.Gun.gun_rotation

    def updateHealthPosition(self):
        if self.healthHelper: self.healthHelper.updateHealthPosition(self.position)

    def setHealth(self, health):
        self.healthHelper.setHealth(health)

    def heavy_fire(self):
        self.Gun.fireFirstWeapon()

    def fire(self):
        self.Gun.fireSecondWeapon()

    def destroy(self):
        animation = ExplosionTankAnimation()
        animation.appendAnimationToLayer(self.position)

        #removeTankFromGame(self)

    def damage(self, bullet):
        x, y = self.position
        x2, y2 = bullet.position
        deltax = math.pow(x - x2, 2)
        deltay = math.pow(y - y2, 2)
        delta = (deltax + deltay)
        range = math.sqrt(delta)
        range = range - (self.width + self.height) * self.scale / 2
        #range = max(range / 4, 1)

        #dmg = bullet.damage - math.pow((( -2 * bullet.damageRadius / math.pow(bullet.damageRadius, 2) ) * math.pi * range), 2)
        dmg = bullet.damage * self.damageKoef(range)
        #print('range: ' + str(range))
        #print('damage (without rand): ' + str(dmg))
        dmg += random.randrange(-bullet.damage / 10, bullet.damage / 10)

        self.health -= dmg

        Global.Queue.append({
            "action": NetworkActions.DAMAGE,
            NetworkDataCodes.TYPE: NetworkDataCodes.TANK,
            NetworkDataCodes.ID: self.id,
            NetworkDataCodes.HEALTH: self.health,
            NetworkDataCodes.DAMAGE: dmg
        })

    def damageKoef(self, range):
        maxRange = 20

        try:
            v = math.log(-1 * range + maxRange, 1.22) + 5
        except ValueError:
            v = 0
        return v / maxRange

    def getObjectFromSelf(self):
        x, y = self.position
        r = self.rotation
        gr = self.gun_rotation

        return {
            'action': NetworkCodes.NetworkActions.UPDATE,
            NetworkCodes.NetworkDataCodes.ID: self.id,
            NetworkCodes.NetworkDataCodes.POSITION: (int(x), int(y)),
            NetworkCodes.NetworkDataCodes.ROTATION: int(r),
            NetworkCodes.NetworkDataCodes.GUN_ROTATION: int(gr),
            NetworkCodes.NetworkDataCodes.CLAN: self.clan,
            NetworkCodes.NetworkDataCodes.HEALTH: self.health,
            NetworkCodes.NetworkDataCodes.TYPE: self.type,
        }