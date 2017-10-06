from objects.Tank import Tank


class TigerTank(Tank):

    type = 8
    spriteName = 'assets/tank/parts/Tiger-II_1.png'
    spriteGunName = 'assets/tank/parts/Tiger-II_.png'

    def __init__(self):
        Tank.__init__(self)
