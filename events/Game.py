from time import sleep
import cocos.collision_model as cm

from components import Global
from components.Collisions import Collisions
from components.Explosion import Explosion


def callUpdatePositions():
    while True:
        updatePositions()
        sleep(0.033)

def callCheckCollisions():
    while True:
        checkCollisions()
        sleep(0.01)

def updatePositions():
    batch = {
        'action': Global.NetworkActions.UPDATE_BATCH,
        'objects': []
    }

    for tank in Global.GameObjects.getTanks():
        #player.setNewPosition()

        try:
            tank.moving_handler.check_position()
        except AttributeError:
            pass

        batch['objects'].append(tank.getObjectFromSelf())

    Global.Queue.append(batch)


def checkCollisions():
    for bullet in Global.GameObjects.getBullets():
        bullet.update()
        bullet.cshape = cm.AARectShape(bullet.position, 2, 2)

        if Collisions.checkWithWalls(bullet) or Collisions.checkWithObjects(bullet, bullet.parent_id) or bullet.exceededTheLengthLimit():
            explosion = Explosion(bullet)
            explosion.checkDamageCollisions()
            bullet.destroy()

    for tank in Global.GameObjects.getTanks():
        if tank.health <= 0:
            tank.destroy()

    for wall in Global.GameObjects.getWalls():
        if wall.health <= 0:
            wall.destroy()

def sendAllTanksToClients():
    for player in Global.GameObjects.getTanks():
        Global.Queue.append(player.getObjectFromSelf())

def sendDataToPlayers():
    updatePerSecond = 40

    while True:
        data = {
            'action': 'update',
            'data': Global.Queue
        }

        Global.Queue = []

        for channel in Global.PullConnsctions:
            channel.Send(data)

        sleep(1.0/updatePerSecond)