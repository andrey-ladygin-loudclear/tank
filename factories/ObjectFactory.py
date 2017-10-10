from Landing.MiniGunTower import MiniGunTower
from components import Global
from components.Global import addObjectToGame
from components.Objects import addGamePlayer
from helpers.TankHelper import TankHelper


class ObjectFactory:

    @staticmethod
    def create(id=0, position=(0,0), clan=1, rotation=0):
        obj = MiniGunTower(id=id, position=position, rotation=rotation, clan=clan)
        addObjectToGame(obj)

        return obj


    @staticmethod
    def getOrCreate(id, position, rotation, clan):

        obj = Global.getGameObject(id)

        if obj: return obj

        return ObjectFactory.create(id=id, position=position, rotation=rotation, clan=clan)
