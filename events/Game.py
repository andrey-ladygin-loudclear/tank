from time import sleep
import cocos.collision_model as cm

from components import Global
from components import NetworkCodes
from components.Collisions import Collisions
from components.Explosion import Explosion
from components.Global import addToQueue, getAllQueue, clearQueue, getGameTanks, getGameBullets, getGameWalls


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
        'action': NetworkCodes.NetworkActions.UPDATE_BATCH,
        'objects': []
    }

    for tank in getGameTanks():
        #player.setNewPosition()

        try:
            tank.moving_handler.check_position()
        except AttributeError:
            pass

        batch['objects'].append(tank.getObjectFromSelf())

    addToQueue(batch)


def checkCollisions():

    for bullet in getGameBullets():
        #bullet.update()
        bullet.cshape = cm.AARectShape(bullet.position, 2, 2)

        if Collisions.checkWithWalls(bullet) or Collisions.checkWithObjects(bullet, bullet.parent_id) or bullet.exceededTheLengthLimit():
            explosion = Explosion(bullet)
            explosion.checkDamageCollisions()

            bullet.destroy()

    for tank in getGameTanks():
        if tank.health <= 0:
            tank.destroy()

    for wall in getGameWalls():
        if wall.health <= 0:
            wall.destroy()

def sendAllTanksToClients():
    for player in getGameTanks():
        addToQueue(player.getObjectFromSelf())

def sendDataToPlayers():
    updatePerSecond = 40

    while True:
        data = {
            'action': 'update',
            'data': getAllQueue()
        }

        clearQueue()

        for channel in Global.PullConnsctions:
            channel.Send(data)

        sleep(1.0/updatePerSecond)