
def main():
    checkGameType()

def checkGameType():
    res = raw_input('1 - create new game, 2 - connect\n')
    clan = raw_input('Select your clan: 1 or 2\n')
    ip = None

    if res == 2:
        ip = raw_input('input ip\n')

    createInterface(clan, res, ip)

def startNewGame():
    print 'start new game'

def connectToGame(ip):
    print 'connect to ' + str(ip)

def createInterface(clan, res, ip):
    # Initialize the window.

    director.director.init(width=3000, height=960, do_not_scale=True, resizable=True)
    #director.director.init(do_not_scale=True, resizable=True, fullscreen=True)

    initGlobalParams()

    # Create a scene and set its initial layer.
    main_scene = scene.Scene(Global.GameLayers.game)
    main_scene.schedule(Global.GameLayers.game.buttonsHandler)

    director.director.on_resize = Global.GameLayers.game.resize
    # Play the scene in the window.
    director.director.run(main_scene)

def initGlobalParams():
    Global.CollisionManager = cm.CollisionManagerBruteForce()
    Global.GameLayers = Layers()
    Global.GameObjects = Objects()

    # Attach a KeyStateHandler to the keyboard object.
    Global.CurrentKeyboard = key.KeyStateHandler()
    director.director.window.push_handlers(Global.CurrentKeyboard)
    #scrollerHandler = layer.ScrollingManager()
    #Global.TankNetworkListenerConnection = NetworkListener('localhost', 1332)

    Global.GameLayers.init()


if __name__ == '__main__':
    main()