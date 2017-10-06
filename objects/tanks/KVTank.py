from objects.Tank import Tank


class KVTank(Tank):

    type = 3
    spriteName = 'assets/tank/parts/KV-2_1.png'
    spriteGunName = 'assets/tank/parts/KV-2_2.png'

    def __init__(self):
        Tank.__init__(self)
