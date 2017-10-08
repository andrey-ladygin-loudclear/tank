from threading import Timer

from cocos import sprite

from components import Global
from objects.weapons.MiniGunWeapon import MiniGunWeapon


class MiniGunTower(sprite.Sprite):
    id = 0
    health = 1000
    type = 5
    clan = 2

    src = 'assets/towers/heavy-murder-final-turret-v2.png'
    weapon = None

    canFire = True
    bulletFreezTime = 0.5

    def __init__(self, position=(0,0)):
        super(MiniGunTower, self).__init__(self.src)
        self.position = position
        self.weapon = MiniGunWeapon()

    def fire(self):
        if not self.canFire: return

        id = Global.getNextId()
        position = self.position
        animation_position = self.position
        rotation = self.rotation - 90
        animation_rotation = self.rotation
        parent_id = self.id

        self.weapon.fire(id=id, position=position, animation_position=animation_position,
                         animation_rotation=animation_rotation, rotation=rotation, parent_id=parent_id)
        self.canFire = False
        Timer(self.bulletFreezTime, self.acceptFire).start()

    def acceptFire(self):
        self.canFire = True