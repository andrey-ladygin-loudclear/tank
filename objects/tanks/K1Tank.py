from objects.Tank import Tank


class K1Tank(Tank):

    type = 2
    spriteName = 'assets/tank/parts/k1.png'
    spriteGunName = 'assets/tank/parts/K2.png'

    def __init__(self):
        Tank.__init__(self)
