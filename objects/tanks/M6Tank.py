from objects.Tank import Tank


class M6Tank(Tank):

    type = 4
    spriteName = 'assets/tank/parts/M-6_1.png'
    spriteGunName = 'assets/tank/parts/M-6_2.png'

    def __init__(self):
        Tank.__init__(self)
