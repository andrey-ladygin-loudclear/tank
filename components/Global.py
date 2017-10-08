import json

import pyglet
from pyglet.window import key
import cocos.collision_model as cm

CurrentKeyboard = key.KeyStateHandler()
CollisionManager = cm.CollisionManagerBruteForce()
PullConnsctions = []

Queue = []
last_id = 0
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

def getGameTanks():
    return tanks

def getGameBullets():
    return bullets

def getGameWalls():
    return walls

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


