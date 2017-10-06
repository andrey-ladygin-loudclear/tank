from threading import Timer

import cocos
from cocos.batch import BatchNode


class Layers:
    globalPanel = None
    stats = None
    walls = []
    backgrounds = []
    bullets = []
    tanks = None

    def __init__(self, main_scene):
        self.bullets = BatchNode()
        self.walls = BatchNode()
        self.backgrounds = BatchNode()
        self.tanks = BatchNode()

        #main_scene = get_main_scene_layer()
        main_scene.add(self.backgrounds, z=0)
        main_scene.add(self.bullets, z=1)
        main_scene.add(self.walls)
        main_scene.add(self.tanks)

        self.globalPanel = cocos.layer.Layer()
        main_scene.add(self.globalPanel, z=1)

        # self.stats = StatsLayer()

    def addElement(self, item, time=0):
        self.globalPanel.add(item)

        if time:
            t = Timer(time, lambda: self.globalPanel.remove(item))
            t.start()

    def addTank(self, tank):
        self.tanks.add(tank)
        self.tanks.add(tank.Gun)
        self.tanks.add(tank.healthHelper)

    def removeTank(self, tank):
        self.tanks.remove(tank)
        self.tanks.remove(tank.Gun)
        self.tanks.remove(tank.healthHelper)

    def addAnimation(self, anim):
        self.globalPanel.add(anim)

    def addWall(self, wall, z):
        self.walls.add(wall, z=z)

    def removeWall(self, wall):
        self.walls.remove(wall)

    def removeAnimation(self, anim):
        if anim in self.globalPanel: self.globalPanel.remove(anim)

    def addBullet(self, bullet):
        self.bullets.add(bullet)

    def removeBullet(self, bullet):
        if bullet in self.bullets: self.bullets.remove(bullet)