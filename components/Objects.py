from random import random

from components.Map import Map
from helpers.TankHelper import TankHelper
from objects.Tank import Tank

last_id = 0
walls = []
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

def addGamePlayer(type, clan, position=(100, 100), rotation=0):
    tank = TankHelper.getTankByType(type)
    #tank = Tank()
    #tank = TankFactory.create(type)
    tank.id = getNextId()
    tank.clan = clan
    # tank.setPosition(position)
    tank.position = position
    tank.rotation = rotation
    #self.sendAllTanksToClients()

    addTankToObjectsAndSprites(tank)

    return tank.id

def removeTankFromGame(tank):
    #if self in Global.GameObjects.getTanks(): Global.GameObjects.removeTank(self)
    pass

def getNextId():
    global last_id
    last_id += 1
    return last_id