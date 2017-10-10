from components import Global
from components.NetworkCodes import NetworkActions


def sendBulletToOtherPlayers(bullet):
    bullet_data = bullet.getObjectFromSelf()
    bullet_data['action'] = NetworkActions.TANK_FIRE

    if Global.IsGeneralServer:
        Global.addToQueue(bullet_data)
    else:
        Global.TankNetworkListenerConnection.Send(bullet_data)


def SendDestroyBulletEvent(bullet):
    bullet_data = bullet.getObjectFromSelf()
    bullet_data['action'] = NetworkActions.DESTROY
    Global.addToQueue(bullet_data)
    # removeBullet({
    #     "action": Global.NetworkActions.DESTROY,
    #     NetworkDataCodes.TYPE: self.type,
    #     NetworkDataCodes.POSITION: self.position,
    #     NetworkDataCodes.ID: self.id
    # })