from random import random

from components.Map import Map

last_id = 0
Walls = []

def getWalls():
    if len(Walls): return Walls

    map = Map()
    map.init_walls()

    for wall in map.get_walls():
        Walls.append(wall.getObjectFromSelf())

    return Walls

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

def addPlayer(self, type):
    tank = TankHelper.getSpriteByTank(type)
    tank.id = self.getNextId()
    tank.clan = 1
    tank.setPosition((100, 100))
    Global.GameObjects.addTank(tank)
    self.sendAllTanksToClients()
    return tank.id



def getNextId(self):
    self.last_id += 1
    return self.last_id