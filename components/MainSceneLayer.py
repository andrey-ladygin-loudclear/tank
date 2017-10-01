from threading import Timer

import PodSixNet
import cocos
from cocos.actions import MoveBy, FadeOut
from pyglet.window import key

from components import Global
from events.NetworkListener import NetworkListener

main_scene = None

def init_main_scene_layer():
    global main_scene
    main_scene = MainSceneLayer()

def get_main_scene_layer():
    return main_scene

class MainSceneLayer(cocos.layer.ScrollableLayer):
    is_event_handler = True
    help = None
    connections_listener = None

    def __init__(self):
        super(MainSceneLayer, self).__init__()
        self.schedule(self.update)

    def update(self, dt):
        if not self.connections_listener: return

        PodSixNet.Connection.connection.Pump()

        if self.connections_listener:
            self.connections_listener.Pump()

    def resize(self, width, height):
        self.viewPoint = (width // 2, height // 2)
        self.currentWidth = width
        self.currentHeight = height

    def buttonsHandler(self, dt):
        x_direction = Global.CurrentKeyboard[key.NUM_4] - Global.CurrentKeyboard[key.NUM_6]
        y_direction = Global.CurrentKeyboard[key.NUM_5] - Global.CurrentKeyboard[key.NUM_8]
        x, y = self.position

        if x_direction:
            x += x_direction * 20

        if y_direction:
            y += y_direction * 20

        if Global.CurrentKeyboard[key.NUM_0]:
            x = y = 0

        if x_direction or y_direction:
            self.set_view(0, 0, self.currentWidth, self.currentHeight, x, y)

        # if self.help:
        #     type = self.selectTank()
        #     if type: self.connectToServer(type)

        #Global.GameLayers.stats.changleStatsPosition(-x, -y, self.currentWidth, self.currentHeight)

    def connectToServer(self, type):
        self.remove(self.help)
        self.help = None
        Global.TankNetworkListenerConnection = NetworkListener('localhost', 1332, type)
        self.TankNetworkListenerConnection = Global.TankNetworkListenerConnection


    label = None

    # def __init__(self):
    #     self.label = cocos.text.Label(
    #         '100',
    #         font_name='Helvetica',
    #         font_size=16,
    #         anchor_x='left',  anchor_y='top'
    #     )
    #     Global.GameLayers.globalPanel.add(self.label)

    def changleStatsPosition(self, x, y, width, height):
        self.label.position = (x, y + height)

    def setHealth(self, health):
        self.label.element.text = str(int(round(health)))

    def damage(self, damage, position):
        label = cocos.text.Label(
            '-' + str(int(round(damage))),
            font_name='Helvetica',
            font_size=10,
            color=(255, 0, 0, 255),
            anchor_x='center',  anchor_y='center'
        )
        label.position = position
        Global.GameLayers.globalPanel.add(label)
        label.do(MoveBy((0, 100), 2) | FadeOut(2))

        t = Timer(2000, lambda: Global.GameLayers.globalPanel.remove(label))
        t.start()