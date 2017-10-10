from time import sleep

from PodSixNet.Channel import Channel

#from helper import Global
from components import Global
from components.NetworkCodes import NetworkActions, NetworkDataCodes
from components.Objects import addGamePlayer
from events.Events import Events


class ClientChannel(Channel):
    events = Events()

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

        if data.get('action') == NetworkActions.TANK_MOVE:
            tank = Global.getGameTank(data.get(NetworkDataCodes.TANK_ID))
            tank.update(data)

        if data.get('action') == NetworkActions.TANK_FIRE:
            self.events.fire(data)

        if data.get('action') == NetworkActions.DAMAGE:
            self.events.damage(data)

