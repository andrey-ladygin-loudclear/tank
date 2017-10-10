from time import sleep

from PodSixNet.Channel import Channel

#from helper import Global
from components import Global
from components.NetworkCodes import NetworkActions, NetworkDataCodes
from components.Objects import addGamePlayer


class ClientChannel(Channel):
    def Network(self, data):
        #print('Network Receive', data)

        if data.get('action') == NetworkActions.INIT:
            index = int(data.get('connection_index'))
            type = data.get(NetworkDataCodes.TYPE)
            clan = data.get(NetworkDataCodes.CLAN)

            channel = Global.PullConnsctions[index]

            id = addGamePlayer(type=type, clan=clan, position=(200, 100))

            channel.Send({
                'action': NetworkActions.INIT,
                'id': id
            })

        tank = Global.getGameTank(data.get(NetworkDataCodes.TANK_ID))

        if data.get('action') == NetworkActions.TANK_MOVE:
            tank.update(data)

        if data.get('action') == NetworkActions.TANK_FIRE:
            if data.get(NetworkDataCodes.TYPE) == NetworkDataCodes.HEAVY_BULLET:
                tank.heavy_fire()

            if data.get(NetworkDataCodes.TYPE) == NetworkDataCodes.STANDART_BULLET:
                tank.fire()

