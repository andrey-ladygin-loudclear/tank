from threading import Timer

import pyglet
from cocos import sprite

from helpers import Global


class StandartBulletFireAnimation:

    def __init__(self):
        explosion = pyglet.image.load('assets/weapons/fire-small-gun.png')
        explosion_seq = pyglet.image.ImageGrid(explosion, 1, 3)
        explosion_tex_seq = pyglet.image.TextureGrid(explosion_seq)
        self.animation = pyglet.image.Animation.from_image_sequence(explosion_tex_seq, .02, loop=False)
        self.anim = sprite.Sprite(self.animation)
        self.anim.scale = 0.2

    def getAnimation(self):
        return self.animation

    def getSprite(self, position, rotation):
        self.anim.position = position
        self.anim.rotation = rotation - 180
        return self.anim

    def appendAnimationToLayer(self, position, rotation):
        anim = self.getSprite(position, rotation)
        Global.GameLayers.addAnimation(anim)
        t = Timer(self.animation.get_duration(), lambda: Global.GameLayers.removeAnimation(anim))
        t.start()