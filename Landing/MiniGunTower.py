from threading import Timer

import math
from cocos import sprite

from components import Global, NetworkCodes
from objects.weapons.MiniGunWeapon import MiniGunWeapon
import cocos.collision_model as cm


class MiniGunTower(sprite.Sprite):
    id = 0
    health = 1000
    type = 5
    clan = 2
    src = 'assets/towers/heavy-murder-final-turret-v2.png'
    weapon = None
    canFire = True
    bulletFreezTime = 0.1

    def __init__(self, id=0, position=(0,0), rotation=0, clan=1):
        super(MiniGunTower, self).__init__(self.src)
        if not id: id = Global.getNextId()

        self.id = id
        self.position = position
        self.rotation = rotation
        self.clan = clan
        self.weapon = MiniGunWeapon()
        self.scale = 0.3

        self.cshape = cm.AARectShape(
            self.position,
            self.width // 2,
            self.height // 2
        )

    def getFirePosition(self, dx, dy):
        cos_x = math.cos(math.radians(self.rotation - 180))
        sin_x = math.sin(math.radians(self.rotation))
        x = self.x + dx * sin_x + dy * cos_x
        y = self.y - dx * cos_x + dy * sin_x
        return (x, y)

    def fire(self):
        if not self.canFire: return

        id = Global.getNextId()
        rotation = self.rotation - 90
        animation_rotation = self.rotation
        parent_id = self.id

        animation_position = self.getFirePosition(-30, -10)
        position = self.getFirePosition(-30, -10)

        self.weapon.fire(id=id, position=position, animation_position=animation_position,
                         animation_rotation=animation_rotation, rotation=rotation, parent_id=parent_id)
        self.canFire = False
        Timer(self.bulletFreezTime, self.acceptFire).start()

    def acceptFire(self):
        self.canFire = True

    def damage(self):
        raise('http://www.bogotobogo.com/python/Multithread/python_multithreading_Event_Objects_between_Threads.php, You should add damage method in MiniGunTower')

    def destroy(self):
        raise('You should add Destroy method in MiniGunTower')

    def getObjectFromSelf(self):
        x, y = self.position
        r = self.rotation

        return {
            'action': NetworkCodes.NetworkActions.UPDATE,
            NetworkCodes.NetworkDataCodes.OBJECT_ID: self.id,
            NetworkCodes.NetworkDataCodes.POSITION: (int(x), int(y)),
            NetworkCodes.NetworkDataCodes.ROTATION: int(r),
            NetworkCodes.NetworkDataCodes.CLAN: self.clan,
            NetworkCodes.NetworkDataCodes.HEALTH: self.health,
        }