from threading import Timer

import PodSixNet
import cocos
from cocos.actions import MoveBy, FadeOut
from pyglet.window import key

from components import Global
from components import NetworkCodes
from components.Global import getGamePlayer
from components.NetworkCodes import NetworkActions, NetworkDataCodes
from events import Game
from events.NetworkListener import NetworkListener


class MainSceneLayer(cocos.layer.ScrollableLayer):
    is_event_handler = True
    help = None
    label = None

    def __init__(self):
        super(MainSceneLayer, self).__init__()
        self.schedule(self.update)

    def update(self, dt):
        if Global.IsGeneralServer:
            Game.checkCollisions()

            if Global.connections_listener: Global.connections_listener.Pump()
        else:
            PodSixNet.Connection.connection.Pump()
            Global.TankNetworkListenerConnection.Pump()
            self.sendDataToServer()

    def sendDataToServer(self):
        player = getGamePlayer()

        if player:
            Global.TankNetworkListenerConnection.Send({
                'action': NetworkActions.TANK_MOVE,
                NetworkDataCodes.POSITION: player.position,
                NetworkDataCodes.GUN_ROTATION: player.gun_rotation,
                NetworkDataCodes.ROTATION: player.rotation,
                NetworkDataCodes.TANK_ID: player.id
            })

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

        self.changleStatsPosition(-x, -y, self.currentWidth, self.currentHeight)

    def connectToServer(self, type):
        self.remove(self.help)
        self.help = None
        Global.TankNetworkListenerConnection = NetworkListener('localhost', 1332, type)
        self.TankNetworkListenerConnection = Global.TankNetworkListenerConnection

    def changleStatsPosition(self, x, y, width, height):
        if self.label:
            self.label.position = (x, y + height)

    def init_panel_with_stats(self):
        self.label = cocos.text.Label(
            str(getGamePlayer().health),
            font_name='Helvetica',
            font_size=16,
            anchor_x='left',  anchor_y='top'
        )

        Global.Layers.globalPanel.add(self.label)

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
        Global.Layers.globalPanel.add(label)
        label.do(MoveBy((0, 100), 2) | FadeOut(2))

        t = Timer(2000, lambda: Global.Layers.globalPanel.remove(label))
        t.start()