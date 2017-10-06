from objects.Tank import Tank


class TankFactory:

    @staticmethod
    def create(id=0, position=(0,0), type=type):
        tank = Tank(type)
        tank.id = id
        tank.position = position

        # if tank.id == Global.CurrentPlayerId:
        #     tank.do(LocalTankMovingHandlers())
        #
        # Global.GameObjects.addTank(tank)
        return tank


    @staticmethod
    def getOrCreate(id, type):
        tank = Global.GameObjects.getTank(id)

        if tank: return tank

        return TankFactory.create(id=id, type=type)

    @staticmethod
    def get(id):
        for tank in Global.GameObjects:
            if tank.id == id:
                return tank

        return None

    # @staticmethod
    # def createTankByClass(tank_class):
    #     if tank_class == 'ETank':
    #         return ETank()
    #
    #     if tank_class == 'KVTank':
    #         return KVTank()