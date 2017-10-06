import cocos
import cocos.collision_model as cm
from cocos import sprite
from cocos.layer import ColorLayer

from components import NetworkCodes
from helpers.HealthHelper import HealthSprite
from objects.Gun import Gun
from objects.animations.ExplosionTankAnimation import ExplosionTankAnimation
from objects.animations.HeavyBulletFireAnimation import HeavyBulletFireAnimation


class Tank(sprite.Sprite):
    Gun = None
    gun_rotation = 0
    id = 0

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