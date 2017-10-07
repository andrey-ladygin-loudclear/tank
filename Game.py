from threading import Thread
from time import sleep

from cocos import director
from cocos import scene

from components import Global
from components.Layers import Layers
from components.MainSceneLayer import MainSceneLayer
from components.Map import Map
from components.Objects import init_global_variables, addGamePlayer, load_map
from events import Game
from events.Network import Network
from events.NetworkListener import NetworkListener


def main():
    createInterface(1, 1, None)
    # res = int(raw_input('1 - create new game, 2 - connect\n'))
    # clan = raw_input('Select your clan: 1 or 2\n')
    # tanktype = int(raw_input('Select your tank type: 1 - 7\n'))
    # ip = None
    #
    # if res == 2:
    #     ip = raw_input('input ip\n')
    #
    # createInterface(tanktype, clan, ip)

def createInterface(tanktype, clan, ip):

    director.director.init(width=3000, height=960, do_not_scale=True, resizable=True)

    # initGlobalParams()

    # Create a scene and set its initial layer.


    main_scene_layer = MainSceneLayer()
    main_scene = scene.Scene(main_scene_layer)
    main_scene.schedule(main_scene_layer.buttonsHandler)

    game_layers = Layers(main_scene_layer)
    init_global_variables(game_layers)


    if ip is None:
        addGamePlayer(type=tanktype, clan=clan, add_moving_handler=True)
        load_map()

        thread = Thread(target = Game.callUpdatePositions)
        thread.setDaemon(True)
        thread.start()

        thread = Thread(target = Game.callCheckCollisions)
        thread.setDaemon(True)
        thread.start()

        thread = Thread(target = connectionsListenersPump)
        thread.setDaemon(True)
        thread.start()
    else:
        main_scene_layer.connections_listener = NetworkListener(ip, 1332, tanktype)


    director.director.on_resize = main_scene_layer.resize
    director.director.window.push_handlers(Global.CurrentKeyboard)
    director.director.run(main_scene)

def connectionsListenersPump():
    connections_listener = Network(localaddr=('localhost', 1332))

    while True:
        connections_listener.Pump()
        sleep(0.0001)

#
#     # Play the scene in the window.1
#
# def initGlobalParams():
#     Global.CollisionManager = cm.CollisionManagerBruteForce()
#     Global.GameLayers = Layers()
#     Global.GameObjects = Objects()
#
#     # Attach a KeyStateHandler to the keyboard object.
#     Global.CurrentKeyboard = key.KeyStateHandler()
#     director.director.window.push_handlers(Global.CurrentKeyboard)
#     #scrollerHandler = layer.ScrollingManager()
#     #Global.TankNetworkListenerConnection = NetworkListener('localhost', 1332)
#
#     Global.GameLayers.init()


if __name__ == '__main__':
    main()