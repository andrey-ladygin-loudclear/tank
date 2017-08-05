from threading import Timer

from cocos import sprite
from pyglet.image import load_animation

from helpers import Global


class ExplosionTankAnimation(sprite.Sprite):

    #src = 'assets/booms/4517769.gif'
    src = 'assets/weapons/Metal-slug-sprites-explosions-001.gif'

    def __init__(self):
        self.animation = load_animation(self.src)
        self.animation.frames[-1].duration = None # stop loop

        super(ExplosionTankAnimation, self).__init__(self.animation)

        self.anim = sprite.Sprite(self.animation)
        self.anim.image_anchor = (self.animation.get_max_width() / 2, self.animation.get_max_height() / 4)
        self.anim.scale = 0.5

    def getAnimation(self):
        return self.animation

    def appendAnimationToLayer(self, position):
        self.anim.position = position
        Global.GameLayers.addAnimation(self.anim)
        t = Timer(self.animation.get_duration(), lambda: Global.GameLayers.removeAnimation(self.anim))
        t.start()