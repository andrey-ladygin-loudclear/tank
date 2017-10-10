from pyglet.resource import ResourceNotFoundException

from components import Global
from components.NetworkCodes import NetworkDataCodes
from factories.BulletFactory import BulletFactory
from factories.TankFactory import TankFactory
from objects.Wall import Wall
from objects.animations.HeavyBulletFireAnimation import HeavyBulletFireAnimation
from objects.animations.StandartBulletFireAnimation import StandartBulletFireAnimation
from objects.bullets.HeavyBullet import HeavyBullet
from objects.bullets.StandartBullet import StandartBullet


class Events():

    def update(self, object):
        id = object.get(NetworkDataCodes.TANK_ID)
        position = object.get(NetworkDataCodes.POSITION)
        rotation = object.get(NetworkDataCodes.ROTATION)
        gun_rotation = object.get(NetworkDataCodes.GUN_ROTATION)
        type = object.get(NetworkDataCodes.TYPE)
        clan = object.get(NetworkDataCodes.CLAN)

        tank = TankFactory.getOrCreate(id, type, clan, rotation)

        if id == Global.CurrentPlayerId: return

        tank.rotation = rotation
        tank.gun_rotation = gun_rotation
        tank.position = position

    def fire(self, object):
        instance = None
        animation_instance = None

        last_update_time = object.get(NetworkDataCodes.LAST_UPDATE_TIME)
        parent_id = object.get(NetworkDataCodes.TANK_ID)
        id = object.get(NetworkDataCodes.BULLET_ID)

        if object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.STANDART_BULLET:
            instance = StandartBullet
            animation_instance = StandartBulletFireAnimation

        if object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.HEAVY_BULLET:
            instance = HeavyBullet
            animation_instance = HeavyBulletFireAnimation

        BulletFactory.create(
            instance=instance,
            id=id,
            parent_id=parent_id,
            position=object.get(NetworkDataCodes.POSITION),
            rotation=object.get(NetworkDataCodes.ROTATION),
            last_update_time=float(last_update_time),
            animation_instance=animation_instance,
            animation_position=object.get(NetworkDataCodes.ANIMATION_POSITION),
            animation_rotation=object.get(NetworkDataCodes.ANIMATION_ROTATION),
            add_moving_handler=True
        )

        # tank = Global.getGameTank(parent_id)
        #
        # if object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.STANDART_BULLET:
        #     tank.Gun.weapon2.fire(bullet)
        #
        # if object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.HEAVY_BULLET:
        #     tank.Gun.weapon1.fire(bullet)

    def damage(self, object):
        id = object.get(NetworkDataCodes.TANK_ID)
        dmg = object.get(NetworkDataCodes.DAMAGE)
        health = object.get(NetworkDataCodes.HEALTH)

        tank = Global.getGameTank(id)
        tank.setHealth(health)
        Global.Layers.stats.damage(dmg, tank.position)

        if id == Global.CurrentPlayerId:
            health = object.get(NetworkDataCodes.HEALTH)
            Global.Layers.stats.setHealth(health)

    def destroy(self, object):
        if object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.WALL:
            id = object.get(NetworkDataCodes.ID)
            wall = Global.getGameWall(id)
            wall.destroy()

        if object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.TANK:
            id = object.get(NetworkDataCodes.TANK_ID)
            tank = Global.getGameTank(id)
            tank.destroy()

        if object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.STANDART_BULLET or \
                        object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.HEAVY_BULLET:

            id = object.get(NetworkDataCodes.BULLET_ID)
            position = object.get(NetworkDataCodes.POSITION)
            bullet = Global.getGameBullet(id)
            if not bullet: return

            bullet.destroy(position)

    def set_walls(self, walls):
        for wall in walls:
            src = wall.get(NetworkDataCodes.SRC).replace('assets/', 'assets/map/').replace('backgrounds/', 'assets/backgrounds/')
            type = wall.get(NetworkDataCodes.TYPE)

            try:
                brick_wall = Wall(src, type)
            except ResourceNotFoundException:
                continue

            brick_wall.id = wall.get(NetworkDataCodes.ID)

            x, y = wall.get(NetworkDataCodes.POSITION)

            brick_wall.update_position((x, y))
            brick_wall.type = type
            brick_wall.src = src

            scale = wall.get(NetworkDataCodes.SCALE, None)
            if scale:
                brick_wall.scale = scale

            Global.Layers.addWall(brick_wall, brick_wall.type)
            # Global.addWall(brick_wall, brick_wall.type)
            #
            # if brick_wall.type != 0 and brick_wall.type != 1:
            #     Global.GameObjects.addWall(brick_wall)