
class NetworkDataCodes:
    TANK_CLASS = 't'
    FRACTION = 'f'
    GUN_ROTATION = 'g'
    CLAN = 'cl'
    BOT = 'bot'
    POSITION = 'p'
    LAST_UPDATE_TIME = 'lt'
    ANGLE_OF_DEFLECTION = 'aod'
    ROTATION = 'r'
    TYPE = 'y'
    SRC = 's'
    ID = 'i'
    BULLET_ID = 'bi'
    TANK_ID = 'ti'
    OBJECT_ID = 'oi'
    HEALTH = 'h'
    DAMAGE = 'd'
    PARENT_ID = 'pi'
    ANIMATION_POSITION = 'ap'
    ANIMATION_ROTATION = 'ar'

    KVTank = 'k'
    ETank = 'e'
    PLAYER = 'p'
    TANK = 't'
    BULLET = 'b'
    STANDART_BULLET = 'StandartBullet'
    HEAVY_BULLET = 'HeavyBullet'
    LIGHT_BULLET = 'LightBullet'
    WALL = 'w'
    SCALE = 'sc'


class NetworkActions:
    INIT = '1'
    TANK_MOVE = '2'
    UPDATE = '3'
    TANK_FIRE = '4'
    DESTROY = '5'
    TEST = '6'
    DAMAGE = '7'
    UPDATE_BATCH = '8'