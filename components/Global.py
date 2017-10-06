from pyglet.window import key
import cocos.collision_model as cm

CurrentKeyboard = key.KeyStateHandler()
CollisionManager = cm.CollisionManagerBruteForce()
PullConnsctions = []

Queue = []

def addToQueue(event):
    global Queue
    Queue.append(event)

def getAllQueue():
    global Queue
    return Queue

def clearQueue():
    global Queue
    Queue = []