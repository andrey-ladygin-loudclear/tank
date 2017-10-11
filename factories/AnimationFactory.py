from components.NetworkCodes import NetworkDataCodes
from objects.animations.HeavyBulletFireAnimation import HeavyBulletFireAnimation
from objects.animations.StandartBulletFireAnimation import StandartBulletFireAnimation


class AnimationFactory:

    @staticmethod
    def create(bullet, firedTank, rotation):
        if isinstance(bullet, StandartBullet):
            animation = standartBulletFireAnimation()
            animatiom_position = firedTank.Gun.standartFireAnimationPosition()
        else:
            animation = heavyBulletFireAnimation()
            animatiom_position = firedTank.Gun.heavyFireAnimationPosition()

        animation.appendAnimationToLayer(animatiom_position, rotation)



    @staticmethod
    def get_instance(type):
        if type == NetworkDataCodes.STANDART_BULLET:
            return StandartBulletFireAnimation

        if type == NetworkDataCodes.HEAVY_BULLET:
            return HeavyBulletFireAnimation



    @staticmethod
    def createAnimationByBulletClass(bullet_class):
        if bullet_class == 'HeavyBullet':
            return HeavyBullet()

        if bullet_class == 'StandartBullet':
            return standartBulletFireAnimation()