import math
import random


class DamageHelper:
    @staticmethod
    def get_damage(position, bullet, dx):
        x, y = position
        x2, y2 = bullet.position
        deltax = math.pow(x - x2, 2)
        deltay = math.pow(y - y2, 2)
        delta = (deltax + deltay)
        range = math.sqrt(delta)
        range = range - dx
        #range = max(range / 4, 1)

        #dmg = bullet.damage - math.pow((( -2 * bullet.damageRadius / math.pow(bullet.damageRadius, 2) ) * math.pi * range), 2)
        dmg = bullet.damage * DamageHelper.damageKoef(range)
        #print('range: ' + str(range))
        #print('damage (without rand): ' + str(dmg))
        dmg += random.randrange(-bullet.damage / 10, bullet.damage / 10)

        return max(1,dmg)

    @staticmethod
    def damageKoef(range):
        maxRange = 20

        try:
            v = math.log(-1 * range + maxRange, 1.22) + 5
        except ValueError:
            v = 0
        return v / maxRange
