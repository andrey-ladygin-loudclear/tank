import pyglet
from cocos import sprite

from components import Global
from components.Global import addanimationToGame

# anim = None
# animation = None
#
# def init_animation():
#     global animation, anim
#     explosion = pyglet.image.load('assets/weapons/fire-small-gun.png')
#     explosion_seq = pyglet.image.ImageGrid(explosion, 1, 3)
#     explosion_tex_seq = pyglet.image.TextureGrid(explosion_seq)
#     animation = pyglet.image.Animation.from_image_sequence(explosion_tex_seq, .02, loop=False)
#     anim = sprite.Sprite(animation)
#     anim.scale = 0.2

class StandartBulletFireAnimation:

    def __init__(self):
        explosion = pyglet.image.load('assets/weapons/fire-small-gun.png')
        explosion_seq = pyglet.image.ImageGrid(explosion, 1, 3)
        explosion_tex_seq = pyglet.image.TextureGrid(explosion_seq)
        self.animation = pyglet.image.Animation.from_image_sequence(explosion_tex_seq, .02, loop=False)
        self.anim = sprite.Sprite(self.animation)
        self.anim.scale = 0.2

    def getAnimation(self):
        return Global.animation

    def getSprite(self, position, rotation):
        Global.anim.position = position
        Global.anim.rotation = rotation - 180
        return Global.anim

    def appendAnimationToLayer(self, position, rotation):
        anim = self.getSprite(position, rotation)
        duration = Global.animation.get_duration()

        addanimationToGame(anim, duration)