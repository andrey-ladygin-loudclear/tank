from components import Global
from components.Objects import addGamePlayer
from helpers.TankHelper import TankHelper


class TankFactory:

    @staticmethod
    def create(id=0, position=(0,0), type=1, clan=1, rotation=0, bot=False):
        add_moving_handler = False

        if id == Global.CurrentPlayerId:
            add_moving_handler = True

        addGamePlayer(type, clan, position=position, rotation=rotation, add_moving_handler=add_moving_handler, id=id, bot=bot)

        tank = Global.getGameTank(id)

        if id == Global.CurrentPlayerId:
            Global.Layers.init_panel_with_stats()

        return tank


    @staticmethod
    def getOrCreate(id, type, clan, rotation, bot):

        tank = Global.getGameTank(id)

        if tank: return tank

        return TankFactory.create(id=id, type=type, clan=clan, rotation=rotation, bot=bot)
