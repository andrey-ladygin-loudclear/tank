from time import time

from components import Global
from components.Global import addBulletToGame
from components.NetworkCodes import NetworkDataCodes
from movingHandlers.BulletMovingHandlers import BulletMovingHandlers
from objects.bullets.HeavyBullet import HeavyBullet
from objects.bullets.StandartBullet import StandartBullet


class BulletFactory:

    @staticmethod
    def create(instance, parent_id, position, rotation=0, last_update_time=time(),
               id=None, animation_instance=None, animation_position=None, animation_rotation=None, add_moving_handler=None):

        if not id: id = Global.getNextId()
        if not animation_position: animation_position = position
        if not animation_rotation: animation_rotation = rotation

        bullet = instance()
        bullet.id = id
        bullet.parent_id = parent_id
        bullet.position = position
        bullet.start_position = position
        bullet.rotation = rotation
        bullet.last_update_time = last_update_time

        bullet.animation_position = animation_position
        bullet.animation_rotation = animation_rotation

        addBulletToGame(bullet)

        if add_moving_handler:
            bullet.do(BulletMovingHandlers())

        if animation_instance:
            animation = animation_instance()
            animation.appendAnimationToLayer(animation_position, animation_rotation)

        return bullet

    @staticmethod
    def get_instance(type):
        if type == NetworkDataCodes.STANDART_BULLET:
            return StandartBullet

        if type == NetworkDataCodes.HEAVY_BULLET:
            return HeavyBullet

    # @staticmethod
    # def create(bullet, id, tank, position, rotation, last_update_time):
    #     bullet.id = id
    #     bullet.parent_id = tank.id
    #     bullet.position = position
    #     bullet.start_position = position
    #     bullet.rotation = rotation
    #     bullet.last_update_time = last_update_time
    #
    #     AnimationFactory.create(bullet, tank, rotation)
    #     #BulletFactory.addToObjects(bullet)
    #     #Global.GameObjects.addBullet(bullet)
    #     bullet.do(BulletMovingHandlers())
    #     return bullet