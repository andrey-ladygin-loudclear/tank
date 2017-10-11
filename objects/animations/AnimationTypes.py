from cocos import sprite

from components import Global


class OnceAnimation(sprite.Sprite):
    def on_animation_end(self):
        self.delete()
        Global.Layers.removeAnimation(self)