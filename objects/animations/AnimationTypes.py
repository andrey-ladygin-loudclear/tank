from cocos import sprite

from components import Global


class OnceAnimation(sprite.Sprite):
    def on_animation_end(self):
        Global.Layers.removeAnimation(self)
        self.delete()