from objects.Tank import Tank


class ETank(Tank):

    type = 1
    spriteName = 'assets/tank/parts/E-100_1.png'
    spriteGunName = 'assets/tank/parts/E-100_2.png'

    def __init__(self):
        Tank.__init__(self)
