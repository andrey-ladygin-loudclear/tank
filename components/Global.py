from pyglet.window import key
import cocos.collision_model as cm

from components.MainScene import MainScene

CurrentKeyboard = key.KeyStateHandler()

CollisionManager = cm.CollisionManagerBruteForce()

MainScene = MainScene()