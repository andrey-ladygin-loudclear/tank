from components import Global
from components.NetworkCodes import NetworkActions


def sendBulletToOtherPlayers(bullet):
    bullet_data = bullet.getObjectFromSelf()
    bullet_data['action'] = NetworkActions.TANK_FIRE

    if Global.IsGeneralServer:
        Global.addToQueue(bullet_data)
    else:
        Global.TankNetworkListenerConnection.Send(bullet_data)