from pyglet.resource import ResourceNotFoundException

from components import Global
from components.NetworkCodes import NetworkDataCodes
from factories.TankFactory import TankFactory
from objects.Wall import Wall


class Events():

    def update(self, object):
        id = object.get(NetworkDataCodes.ID)
        position = object.get(NetworkDataCodes.POSITION)
        rotation = object.get(NetworkDataCodes.ROTATION)
        gun_rotation = object.get(NetworkDataCodes.GUN_ROTATION)
        type = object.get(NetworkDataCodes.TYPE)

        tank = TankFactory.getOrCreate(id, type)

        if id == Global.CurrentPlayerId: return

        tank.rotation = rotation
        tank.gun_rotation = gun_rotation
        tank.position = position

    def fire(self, object):
        id = object.get(NetworkDataCodes.ID)
        parent_id = object.get(NetworkDataCodes.PARENT_ID)
        position = object.get(NetworkDataCodes.POSITION)
        rotation = object.get(NetworkDataCodes.ROTATION)

        last_update_time = object.get(NetworkDataCodes.LAST_UPDATE_TIME)
        last_update_time = float(last_update_time)

        tank = Global.getGameTank(parent_id)

        if object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.STANDART_BULLET:
            tank.Gun.weapon2.fire(id, position, rotation, last_update_time)

        if object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.HEAVY_BULLET:
            tank.Gun.weapon1.fire(id, position, rotation, last_update_time)

    def damage(self, object):
        id = object.get(NetworkDataCodes.ID)
        dmg = object.get(NetworkDataCodes.DAMAGE)
        health = object.get(NetworkDataCodes.HEALTH)

        print('id', id)
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
            id = object.get(NetworkDataCodes.ID)
            tank = Global.getGameTank(id)
            tank.destroy()

        if object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.STANDART_BULLET or \
                        object.get(NetworkDataCodes.TYPE) == NetworkDataCodes.HEAVY_BULLET:

            id = object.get(NetworkDataCodes.ID)
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