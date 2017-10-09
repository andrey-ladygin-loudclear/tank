from time import sleep

from PodSixNet.Channel import Channel

#from helper import Global
from components import Global
from components.NetworkCodes import NetworkActions, NetworkDataCodes
from components.Objects import addGamePlayer


class ClientChannel(Channel):
    def Network(self, data):
        print('Network Receive', data)

        if data.get('action') == NetworkActions.INIT:
            index = int(data.get('connection_index'))
            type = data.get('type')
            clan = data.get('clan')
            channel = Global.PullConnsctions[index]
            #id = Global.game.addPlayer(type)
            id = addGamePlayer(type=type, clan=clan)
            print('addGamePlayer', id)
            channel.Send({
                'action': NetworkActions.INIT,
                'id': id
            })

        for player in Global.getGameTanks():
            if player.id == data.get('id'):

                if data.get('action') == NetworkActions.TANK_MOVE:
                    player.update(data)

                if data.get('action') == NetworkActions.TANK_FIRE:
                    if data.get('type') == NetworkDataCodes.HEAVY_BULLET:
                        player.heavy_fire()

                    if data.get('type') == NetworkDataCodes.STANDART_BULLET:
                        player.fire()

