from os.path import join
from random import random
import json

from cocos import sprite
from pyglet.resource import ResourceNotFoundException

from Landing.LandingObject import LandingObject
from Landing.Tower import Tower
from components.Map import Map
from components.NetworkCodes import NetworkDataCodes
from helpers.TankHelper import TankHelper
from movingHandlers.DefaultTankMovingHandlers import DefaultTankMovingHandlers
from movingHandlers.TowerMovingHandlers import TowerMovingHandlers
from objects.Tank import Tank
from objects.Wall import Wall

last_id = 0
walls = []
all_walls = []
tanks = []
bullets = []
Layers = None

def init_global_variables(game_layers):
    global Layers
    Layers = game_layers

def getWalls():
    if len(walls): return walls

    map = Map()
    map.init_walls()

    for wall in map.get_walls():
        walls.append(wall.getObjectFromSelf())

    return walls

def getGameTanks():
    return tanks

def getGameBullets():
    return bullets

def getGameWalls():
    return walls

def addTankToObjectsAndSprites(tank):
    tanks.append(tank)
    Layers.addTank(tank)


def get_map():
    with open('map2/exportMap.json', 'r') as f:
        read_data = f.read()

    return json.loads(read_data)

def load_map():
    for wall in get_map():
        wall = LandingObject(wall)
        wall.id = getNextId()
        all_walls.append(wall)

        if wall.type != 0 and wall.type != 1:
            walls.append(wall)

    set_walls()

def add_background():
    name = 'assets/backgrounds/fill.png'
    spriteObj = sprite.Sprite(name)
    spriteObj.src = name
    spriteObj.position = (0, 0)
    spriteObj.type = 0
    spriteObj.image_anchor = (0, 0)
    Layers.addWall(spriteObj)

def add_clans_objects():
    tower = Tower(position=(300, 300))
    tower.do(TowerMovingHandlers())
    Layers.addWall(tower, z=5)

def set_walls():
    add_background()

    for wall in all_walls:
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

        Layers.addWall(brick_wall, brick_wall.type)

    add_clans_objects()

def addBot(self, position=(0,0), rotation=0, clan=0, type=1):
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

def addGamePlayer(type, clan, position=(100, 100), rotation=0, add_moving_handler=False):
    tank = TankHelper.getTankByType(type)
    #tank = Tank()
    #tank = TankFactory.create(type)
    tank.id = getNextId()
    tank.clan = clan
    # tank.setPosition(position)
    tank.position = position
    tank.rotation = rotation
    #self.sendAllTanksToClients()
    #if tank.id == Global.CurrentPlayerId:

    if add_moving_handler:
        tank.do(DefaultTankMovingHandlers())

    addTankToObjectsAndSprites(tank)

    return tank.id

def removeTankFromGame(tank):
    #if self in Global.GameObjects.getTanks(): Global.GameObjects.removeTank(self)
    pass

def getNextId():
    global last_id
    last_id += 1
    return last_id