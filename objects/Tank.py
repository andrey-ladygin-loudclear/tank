import cocos.collision_model as cm
from cocos import sprite

from components import NetworkCodes, Global
from components.NetworkCodes import NetworkActions, NetworkDataCodes
from helpers.DamageHelper import DamageHelper
from helpers.HealthHelper import HealthSprite
from objects.Gun import Gun
from objects.animations.ExplosionTankAnimation import ExplosionTankAnimation


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
    speed_acceleration = 1.2
    max_speed = 35


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

    def update(self, data):
        self.position = data.get(NetworkDataCodes.POSITION)
        self.gun_rotation = data.get(NetworkDataCodes.GUN_ROTATION)
        self.rotation = data.get(NetworkDataCodes.ROTATION)

    def updateHealthPosition(self):
        if self.healthHelper: self.healthHelper.updateHealthPosition(self.position)

    def setHealth(self, health):
        self.healthHelper.setHealth(health)

    def heavy_fire(self, bullet=None):
        self.Gun.fireFirstWeapon(bullet)

    def fire(self, bullet=None):
        self.Gun.fireSecondWeapon(bullet)

    def destroy(self):
        animation = ExplosionTankAnimation()
        animation.appendAnimationToLayer(self.position)

        Global.EventDispatcher.dispatch_event('tank_destroy', self)
        Global.removeTankFromGame(self)

    def damage(self, bullet):
        dx = (self.width + self.height) * self.scale / 2
        dmg = DamageHelper.get_damage(self.position, bullet, dx)

        self.health -= dmg

        Global.damageSomeTank(id=self.id, dmg=dmg, health=self.health)

        Global.Queue.append({
            "action": NetworkActions.DAMAGE,
            NetworkDataCodes.TYPE: NetworkDataCodes.TANK,
            NetworkDataCodes.TANK_ID: self.id,
            NetworkDataCodes.HEALTH: self.health,
            NetworkDataCodes.DAMAGE: dmg
        })

    def getGunRotation(self):
        return self.gun_rotation + self.rotation

    def getObjectFromSelf(self):
        x, y = self.position
        r = self.rotation
        gr = self.gun_rotation

        return {
            'action': NetworkCodes.NetworkActions.UPDATE,
            NetworkCodes.NetworkDataCodes.TANK_ID: self.id,
            NetworkCodes.NetworkDataCodes.POSITION: (int(x), int(y)),
            NetworkCodes.NetworkDataCodes.ROTATION: int(r),
            NetworkCodes.NetworkDataCodes.GUN_ROTATION: int(gr),
            NetworkCodes.NetworkDataCodes.CLAN: self.clan,
            NetworkCodes.NetworkDataCodes.HEALTH: self.health,
            NetworkCodes.NetworkDataCodes.TYPE: self.type,
        }