from cocos import director
from cocos import scene

from components import Global
#from components.MovableScreen import MovableScreen

#from components.MainScene import MainSceneInstance
from components.MainScene import getMainSceneInstance


def main():
    res = raw_input('1 - create new game, 2 - connect\n')
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

    MainSceneInstance = getMainSceneInstance()

    main_scene = scene.Scene(MainSceneInstance)
    main_scene.schedule(MainSceneInstance.buttonsHandler)

    director.director.on_resize = MainSceneInstance.resize
    director.director.window.push_handlers(Global.CurrentKeyboard)
    director.director.run(main_scene)
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