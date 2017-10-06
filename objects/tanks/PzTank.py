from objects.Tank import Tank


class PzTank(Tank):

    type = 5
    spriteName = 'assets/tank/parts/Pz.1.png'
    spriteGunName = 'assets/tank/parts/Pz.2.png'

    def __init__(self):
        Tank.__init__(self)
