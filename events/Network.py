from threading import Thread
from time import sleep

from PodSixNet.Server import Server

from components import Global, Objects
#from events.ClientChannel import ClientChannel


class Network(Server):
    #channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)

    def Connected(self, channel, addr):
        print("new connection:", channel)
        ip, port = addr

        Global.PullConnsctions.append(channel)
        index = Global.PullConnsctions.index(channel)

        channel.Send({
            'action': Global.NetworkActions.INIT,
            'connection_index': index
        })

        channel.Send({
            'action': Global.NetworkActions.INIT,
            'walls': Objects.getWalls(),
        })

    def close(self):
        Server.close(self)
        print 'close'