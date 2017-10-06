from objects.tanks.ETank import ETank
from objects.tanks.K1Tank import K1Tank
from objects.tanks.KVTank import KVTank
from objects.tanks.M6Tank import M6Tank
from objects.tanks.Pz2Tank import Pz2Tank
from objects.tanks.PzTank import PzTank
from objects.tanks.T34Tank import T34Tank
from objects.tanks.TigerTank import TigerTank


class TankHelper():

    @staticmethod
    def getTankByType(type):
        if type == 1: return ETank()
        if type == 2: return K1Tank()
        if type == 3: return KVTank()
        if type == 4: return M6Tank()
        if type == 5: return PzTank()
        if type == 6: return Pz2Tank()
        if type == 7: return T34Tank()
        if type == 8: return TigerTank()

    # @staticmethod
    # def getSpriteByTank(type):
    #     if type == 1: return 'assets/tank/parts/E-100_1.png'
    #     if type == 2: return 'assets/tank/parts/k1.png'
    #     if type == 3: return 'assets/tank/parts/KV-2_1.png'
    #     if type == 4: return 'assets/tank/parts/M-6_1.png'
    #     if type == 5: return 'assets/tank/parts/Pz.1.png'
    #     if type == 6: return 'assets/tank/parts/Pz.2-1.png'
    #     if type == 7: return 'assets/tank/parts/T34_1.png'
    #     if type == 8: return 'assets/tank/parts/Tiger-II_1.png'
    #
    # @staticmethod
    # def getGunSpriteByTank(type):
    #     if type == 1: return 'assets/tank/parts/E-100_2.png'
    #     if type == 2: return 'assets/tank/parts/K2.png'
    #     if type == 3: return 'assets/tank/parts/KV-2_2.png'
    #     if type == 4: return 'assets/tank/parts/M-6_2.png'
    #     if type == 5: return 'assets/tank/parts/Pz.2.png'
    #     if type == 6: return 'assets/tank/parts/Pz.2-2.png'
    #     if type == 7: return 'assets/tank/parts/T34_2.png'
    #     if type == 8: return 'assets/tank/parts/Tiger-II_.png'









