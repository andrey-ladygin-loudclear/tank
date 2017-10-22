from threading import Timer

import cocos
from cocos.batch import BatchNode


class Layers:
    globalPanel = None
    stats = None
    walls = []
    objects = []
    backgrounds = []
    bullets = []
    tanks = None

    main_scene = None

    def __init__(self, main_scene):
        self.bullets = BatchNode()
        self.walls = BatchNode()
        self.objects = BatchNode()
        self.backgrounds = BatchNode()
        self.tanks = BatchNode()
        # self.decorations = BatchNode()

        #main_scene = get_main_scene_layer()
        self.main_scene = main_scene
        self.main_scene.add(self.backgrounds, z=0)
        self.main_scene.add(self.bullets, z=1)
        # self.main_scene.add(self.decorations)
        self.main_scene.add(self.walls)
        self.main_scene.add(self.objects)
        self.main_scene.add(self.tanks)

        self.globalPanel = cocos.layer.Layer()
        self.main_scene.add(self.globalPanel, z=1)

        # self.stats = StatsLayer()

    def init_panel_with_stats(self):
        self.main_scene.init_panel_with_stats()

    def setHealth(self, health):
        self.main_scene.setHealth(health)

    def damage(self, damage, position):
        self.main_scene.damage(damage, position)

    def addElement(self, item, time=0):
        self.globalPanel.add(item)

        if time:
            t = Timer(time, lambda: self.globalPanel.remove(item))
            t.start()

    tankz = 3

    def addTank(self, tank):
        self.tankz += 1
        print(tank.position)
        self.tanks.add(tank, z=2)
        self.tanks.add(tank.Gun, z=3)
        self.tanks.add(tank.healthHelper, z=4)

    def removeTank(self, tank):
        self.tanks.remove(tank)
        self.tanks.remove(tank.Gun)
        self.tanks.remove(tank.healthHelper)

    def addAnimation(self, anim):
        self.globalPanel.add(anim)

    def addObject(self, obj, z=0):
        self.objects.add(obj, z=z)

        if obj.healthHelper:
            self.objects.add(obj.healthHelper, z=2)

    def removeObject(self, obj):
        self.objects.remove(obj)

        if obj.healthHelper:
            self.objects.remove(obj.healthHelper)

    def addWall(self, wall, z=0):
        self.walls.add(wall, z=z)

    def removeWall(self, wall):
        self.walls.remove(wall)

    def removeAnimation(self, anim):
        self.globalPanel.remove(anim)
        # try:
        #     if anim in self.globalPanel: self.globalPanel.remove(anim)
        # except Exception:
        #     pass

    def addBullet(self, bullet):
        self.bullets.add(bullet)

    def removeBullet(self, bullet):
        if bullet in self.bullets: self.bullets.remove(bullet)