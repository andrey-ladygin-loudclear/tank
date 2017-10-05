from threading import Thread

from cocos import director
from cocos import scene

from components import Global
from components.MainSceneLayer import MainSceneLayer, init_main_scene_layer, get_main_scene_layer
from components.Map import Map
from events import Game
from events.Network import Network
from events.NetworkListener import NetworkListener


def main():
    res = int(raw_input('1 - create new game, 2 - connect\n'))
    clan = raw_input('Select your clan: 1 or 2\n')
    tanktype = raw_input('Select your tank type: 1 - 7\n')
    ip = None

    if res == 2:
        ip = raw_input('input ip\n')

    createInterface(tanktype, clan, res, ip)

def createInterface(tanktype, clan, res, ip):

    director.director.init(width=3000, height=960, do_not_scale=True, resizable=True)

    # initGlobalParams()

    # Create a scene and set its initial layer.

    # Global.MainScene = MainSceneLayer()
    init_main_scene_layer()
    main_scene_layer = get_main_scene_layer()
    main_scene = scene.Scene(main_scene_layer)
    main_scene.schedule(main_scene_layer.buttonsHandler)

    director.director.on_resize = main_scene_layer.resize
    director.director.window.push_handlers(Global.CurrentKeyboard)
    director.director.run(main_scene)

    if ip is None:
        # map = Map()
        # map.init_walls()

        main_scene_layer.connections_listener = Network(localaddr=('localhost', 1332))

        thread = Thread(target = Game.callUpdatePositions)
        thread.setDaemon(True)
        thread.start()

        thread = Thread(target = Game.callCheckCollisions)
        thread.setDaemon(True)
        thread.start()
    else:
        main_scene_layer.connections_listener = NetworkListener(ip, 1332, tanktype)
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