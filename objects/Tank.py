import cocos
import cocos.collision_model as cm
from cocos import sprite
from cocos.layer import ColorLayer

from helpers import Global
from helpers.HealthHelper import HealthHelper
from helpers.TankHelper import TankHelper
from objects.Gun import Gun
from objects.animations.ExplosionTankAnimation import ExplosionTankAnimation
from objects.animations.HeavyBulletFireAnimation import HeavyBulletFireAnimation


class Tank(sprite.Sprite):
    Gun = None
    gun_rotation = 0
    id = 0

    speed = 30

    old_position = (0, 0)
    velocity = (0, 0)

    maxBulletsHolder = 10
    bulletsHolder = 10
    timeForBulletsHolderReload = 3

    healthHelper = None

    def __init__(self, type):
        spriteName = TankHelper.getSpriteByTank(type)
        spriteGunName = TankHelper.getGunSpriteByTank(type)

        self.Gun = Gun(spriteGunName, self)
        super(Tank, self).__init__(spriteName)

        self.healthHelper = HealthHelper(self)
        self.scale = self.Gun.scale = 0.5

        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def _update_position(self):
        super(Tank, self)._update_position()
        self.Gun.position = self.position
        self.Gun.rotation = self.rotation + self.gun_rotation

        if self.healthHelper: self.healthHelper.updateHealthPosition()

        # self.rotation = 180
        # self.Gun.position = self.position
        # self.Gun.rotation = self.rotation + self.Gun.gun_rotation

    def setHealth(self, health):
        self.healthHelper.setHealth(health)

    def heavy_fire(self):
        self.Gun.fireFirstWeapon()

    def fire(self):
        self.Gun.fireSecondWeapon()

    def destroy(self):
        animation = ExplosionTankAnimation()
        animation.appendAnimationToLayer(self.position)
        if self in Global.GameObjects.getTanks(): Global.GameObjects.removeTank(self)

        self.healthHelper.destroy()
