#import Global
from objects.animations.heavyBulletFireAnimation import heavyBulletFireAnimation
from objects.animations.standartBulletFireAnimation import standartBulletFireAnimation
from objects.bullets.heavyBullet import HeavyBullet
from objects.bullets.standartBullet import StandartBullet


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
    def createAnimationByBulletClass(bullet_class):
        if bullet_class == 'HeavyBullet':
            return HeavyBullet()

        if bullet_class == 'StandartBullet':
            return standartBulletFireAnimation()