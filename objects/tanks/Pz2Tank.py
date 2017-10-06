from objects.Tank import Tank


class Pz2Tank(Tank):

    type = 6
    spriteName = 'assets/tank/parts/Pz.2-1.png'
    spriteGunName = 'assets/tank/parts/Pz.2-2.png'

    def __init__(self):
        Tank.__init__(self)
