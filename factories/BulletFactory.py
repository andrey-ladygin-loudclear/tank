from factories.AnimationFactory import AnimationFactory
from movingHandlers.BulletMovingHandlers import BulletMovingHandlers
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


class BulletFactory:

    @staticmethod
    def create(bullet, id, tank, position, rotation, last_update_time):
        bullet.id = id
        bullet.parent_id = tank.id
        bullet.position = position
        bullet.start_position = position
        bullet.rotation = rotation
        bullet.last_update_time = last_update_time

        AnimationFactory.create(bullet, tank, rotation)
        #BulletFactory.addToObjects(bullet)
        #Global.GameObjects.addBullet(bullet)
        bullet.do(BulletMovingHandlers())
        return bullet