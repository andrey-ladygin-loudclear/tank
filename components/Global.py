import json
from threading import Timer

import pyglet
from cocos import sprite
from pyglet.image import load_animation
from pyglet.image.atlas import TextureBin
from pyglet.window import key
import cocos.collision_model as cm

from components.GameEventDispatcher import GameEventDispatcher
from components.NetworkCodes import NetworkActions

CurrentKeyboard = key.KeyStateHandler()
CollisionManager = cm.CollisionManagerBruteForce()
PullConnsctions = []
TankNetworkListenerConnection = None
IsGeneralServer = False

MapWidth = 4480
MapHeight = 4480

Queue = []
last_id = 0
CurrentPlayerId = 0
walls = []
all_walls = []
tanks = []
objects = []
bullets = []
Layers = None

connections_listener = None


# def getEnemyCenter(clan):
#     for obj in objects:
#         if isinstance(obj, Center) and obj.clan != clan:
#             return obj

def addObjectToGame(object):
    objects.append(object)
    CollisionManager.add(object)
    Layers.addObject(object)

def addBulletToGame(bullet):
    bullets.append(bullet)
    Layers.addBullet(bullet)

def getGameObjects():
    return objects

def getGameObject(id):
    for obj in getGameObjects():
        if obj.id == id:
            return obj

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

def getGamePlayer():
    return getGameTank(CurrentPlayerId)

def getGameTank(id):
    for tank in getGameTanks():
        if tank.id == id:
            return tank

def getGameTanks():
    return tanks

def removeTankFromGame(tank):
    Layers.removeTank(tank)
    tanks.remove(tank)

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

def addWallToGame(wall):
    CollisionManager.add(wall)
    walls.append(wall)

def addanimationToGame(anim, duration=None):
    Layers.addAnimation(anim)
    if duration:
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

def setCurrentPlayerStats(id):
    global CurrentPlayerId
    CurrentPlayerId = id
    Layers.init_panel_with_stats()

def damageSomeTank(id, health, dmg):
    tank = getGameTank(id)
    tank.setHealth(health)
    Layers.damage(dmg, tank.position)

    if id == CurrentPlayerId:
        Layers.setHealth(health)

def damageSomeObject(id, health, dmg):
    obj = getGameObject(id)
    obj.setHealth(health)
    Layers.damage(dmg, obj.position)



class EventDispatcherInstance(pyglet.event.EventDispatcher):
    #src = 'assets/weapons/bullet-explode.gif'
    src = 'assets/booms/4517769.gif'
    anim = None
    animation = None
    duration = None

    def load_anim(self):
        print('load_anim')
        self.animation = load_animation(self.src)
        #self.bin = TextureBin()
        self.animation.frames[-1].duration = None # stop loop

        #self.anim = sprite.Sprite(self.animation)
        # self.anim = OnceAnimation(self.animation)
        # self.anim.image_anchor = (self.animation.get_max_width() / 2, self.animation.get_max_height() / 4)
        # self.anim.scale = 0.2
        self.duration = self.animation.get_duration() + 1

        #self.anim = OnceAnimation(self.animation.get_transform())

        # @self.animation.event
        # def on_animation_end(clicks):
        #     print('ovverided', clicks)
        #     pass

    def create_animation(self, position):
        return
        if not self.animation: self.load_anim()

        #an = copy(self.anim)
        #an = (self.anim)
        an = OnceAnimation(self.animation)
        #an = self.anim.get_local_transform()
        #an = copy.deepcopy(self.anim)
        an.image_anchor = (self.animation.get_max_width() / 2, self.animation.get_max_height() / 4)
        an.scale = 0.2

        an.position = position
        an.rotation = 0 - 180
        addanimationToGame(an, self.duration)


EventDispatcher = GameEventDispatcher()
EventDispatcher.register_event_type('tank_destroy')


AnimationsQueue = []