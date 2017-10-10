from time import time

from PodSixNet.Connection import ConnectionListener, connection

from components import Global
from components.NetworkCodes import NetworkActions, NetworkDataCodes
from events.Events import Events


class NetworkListener(ConnectionListener):
    events = Events()

    def __init__(self, host, port, type, clan):
        self.Connect((host, port))
        self.type = type
        self.clan = clan

    def Network(self, update):
        print(update)
        #print time(), update

        if update.get('action') == NetworkActions.INIT:
            if update.get('walls'):
                self.events.set_walls(update.get('walls'))

            if update.get('id') and update.get('id'):
                Global.CurrentPlayerId = int(update.get('id'))

            if update.get('connection_index', -1) != -1:
                Global.TankNetworkListenerConnection.Send({
                    'action': NetworkActions.INIT,
                    NetworkDataCodes.TYPE: self.type,
                    NetworkDataCodes.CLAN: self.clan,
                    'connection_index': str(update.get('connection_index')),
                })

        for data in update.get('data', []):

            if data.get('action') == NetworkActions.UPDATE:
                self.events.update(data)

            if data.get('action') == NetworkActions.UPDATE_BATCH:
                for player_data in data.get('objects'):
                    self.events.update(player_data)

            if data.get('action') == NetworkActions.TANK_FIRE:
                self.events.fire(data)

            if data.get('action') == NetworkActions.DAMAGE:
                self.events.damage(data)

            if data.get('action') == NetworkActions.DESTROY:
                self.events.destroy(data)

    #https://www.youtube.com/watch?v=AdG_ITCFHDI EXPLODIONS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

    def Network_connected(self, data):
        print "connected to the server"

    def Network_error(self, data):
        print(data['error'])

    def Network_disconnected(self, data):
        print "disconnected from the server"
