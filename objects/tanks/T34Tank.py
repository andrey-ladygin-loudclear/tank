from objects.Tank import Tank


class T34Tank(Tank):

    type = 7
    spriteName = 'assets/tank/parts/T34_1.png'
    spriteGunName = 'assets/tank/parts/T34_2.png'

    def __init__(self):
        Tank.__init__(self)
