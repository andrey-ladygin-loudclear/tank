from random import random

from cocos import sprite
from pyglet.resource import ResourceNotFoundException

from Landing.Center import Center
from Landing.LandingObject import LandingObject

from Landing.MiniGunTower import MiniGunTower
from components import Global
from components.Global import addObjectToGame
from helpers.TankHelper import TankHelper
from movingHandlers.BotTankMovingHandlers import BotTankMovingHandlers
from movingHandlers.DefaultTankMovingHandlers import DefaultTankMovingHandlers
from movingHandlers.TowerMovingHandlers import TowerMovingHandlers
from movingHandlers.UserTankMovingHandlers import UserTankMovingHandlers
from objects.Tank import Tank
from objects.Wall import Wall




def load_map():
    for wall in Global.get_map():
        wall = LandingObject(wall)
        wall.id = Global.getNextId()
        Global.all_walls.append(wall)

        if wall.type != 0 and wall.type != 1:
            Global.walls.append(wall)

    set_walls()


def add_background():
    name = 'assets/backgrounds/fill.png'
    spriteObj = sprite.Sprite(name)
    spriteObj.src = name
    spriteObj.position = (0, 0)
    spriteObj.type = 0
    spriteObj.image_anchor = (0, 0)
    Global.Layers.addWall(spriteObj)

def add_clans_objects():
    tower = MiniGunTower(position=(1000, 2320), clan=2)
    tower.do(TowerMovingHandlers())
    addObjectToGame(tower)
    tower = MiniGunTower(position=(1240, 2320), clan=2)
    tower.do(TowerMovingHandlers())
    addObjectToGame(tower)


    tower = MiniGunTower(position=(1000, 1520), clan=1, rotation=180)
    tower.do(TowerMovingHandlers())
    addObjectToGame(tower)

    tower = MiniGunTower(position=(1240, 1520), clan=1, rotation=180)
    tower.do(TowerMovingHandlers())
    addObjectToGame(tower)



    center = Center(position=(1120, 3740), clan=2)
    addObjectToGame(center)
    center = Center(position=(1120, 100), clan=1)
    addObjectToGame(center)

def set_walls():
    add_background()

    for wall in Global.all_walls:
        #src = wall.get(NetworkDataCodes.SRC).replace('assets/', 'assets/map/')
        src = wall.src.replace('assets/', 'assets/map/')
        type = wall.type

        try:
            brick_wall = Wall(src, type)
        except ResourceNotFoundException:
            continue

        #brick_wall.id = wall.get(NetworkDataCodes.ID)
        brick_wall.id = wall.id
        #x, y = wall.get(NetworkDataCodes.POSITION)
        x, y = wall.position

        brick_wall.update_position((x, y))
        brick_wall.type = type
        brick_wall.src = src

        #scale = wall.get(NetworkDataCodes.SCALE, None)
        scale = wall.scale
        if scale: brick_wall.scale = scale

        Global.Layers.addWall(brick_wall, brick_wall.type)

    add_clans_objects()

def addBot(type, clan, position=(100, 100), rotation=0, add_moving_handler=False, id=None):
    tank = Tank()
    tank.id = self.getNextId()
    tank.bot = True
    tank.setPosition(position)
    tank.rotation = rotation
    tank.clan = clan
    tank.type = type
    tank.gun_rotation = random.randrange(1, 360)

    #moving_handler = BotTankMovingHandlers(tank)
    #moving_handler.setDaemon(True)
    #moving_handler.start()
    tank.moving_handler = BotTankMovingHandlers(tank)

    Global.GameObjects.addTank(tank)

    self.sendAllTanksToClients()

    return tank.id

def addGamePlayer(type, clan, position=(100, 100), rotation=0, add_moving_handler=False, id=None, bot=False):
    tank = TankHelper.getTankByType(int(type))

    if id:
        tank.id = id
    else:
        tank.id = Global.getNextId()

    tank.clan = clan
    tank.bot = bot
    tank.position = position
    # tank.gun_rotation = rotation
    tank.rotation = rotation
    #self.sendAllTanksToClients()

    if add_moving_handler:
        tank.do(UserTankMovingHandlers())

    if bot:
        tank.do(BotTankMovingHandlers())
        # tank.moving_handler = BotTankMovingHandlers(tank)
        # tank.moving_handler.start()

    Global.addTankToObjectsAndSprites(tank)

    return tank.id
