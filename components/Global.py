import json
from threading import Timer

import pyglet
from pyglet.window import key
import cocos.collision_model as cm

CurrentKeyboard = key.KeyStateHandler()
CollisionManager = cm.CollisionManagerBruteForce()
PullConnsctions = []
TankNetworkListenerConnection = None

Queue = []
last_id = 0
CurrentPlayerId = 0
walls = []
all_walls = []
tanks = []
bullets = []
Layers = None

def addBulletToGame(bullet):
    bullets.append(bullet)
    Layers.addBullet(bullet)

def addToQueue(event):
    global Queue
    Queue.append(event)

def getAllQueue():
    return Queue

def clearQueue():
    global Queue
    Queue = []

def init_global_variables(game_layers):
    global Layers
    Layers = game_layers

def getGameTank(id):
    for tank in getGameTanks():
        if tank.id == id:
            return tank

def getGameTanks():
    return tanks

def getGameBullet(id):
    for bullet in getGameBullets():
        if bullet.id == id:
            return bullet

def getGameBullets():
    return bullets

def removeBullet(bullet):
    Layers.removeBullet(bullet)
    if bullet in bullets: bullets.remove(bullet)

def getGameWall(id):
    for wall in getGameWalls():
        if wall.id == id:
            return wall

def getGameWalls():
    return walls

def addnimationToGame(anim, duration):
    Layers.addAnimation(anim)
    t = Timer(duration, lambda: Layers.removeAnimation(anim))
    t.start()

def addTankToObjectsAndSprites(tank):
    CollisionManager.add(tank)
    tanks.append(tank)
    Layers.addTank(tank)

def get_map():
    with open('map2/exportMap.json', 'r') as f:
        read_data = f.read()

    return json.loads(read_data)

def getNextId():
    global last_id
    last_id += 1
    return last_id


