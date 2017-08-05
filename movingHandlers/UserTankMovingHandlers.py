from time import time, sleep

import Global
from movingHandlers.DefaultTankMovingHandlers import DefaultTankMovingHandlers
from pyglet.window import key
from cocos import actions


class UserTankMovingHandlers(actions.Move):

    RIGHT = key.RIGHT
    LEFT = key.LEFT
    UP = key.UP
    DOWN = key.DOWN
    GUN_LEFT = key.Q
    GUN_RIGHT = key.E
    FIRE_HEAVY_GUN = key.SPACE
    FIRE_LIGHT_GUN = key.W

    # step() is called every frame.
    # dt is the number of seconds elapsed since the last call.
    def step(self, dt):
        super(UserTankMovingHandlers, self).step(dt) # Run step function on the parent OF PARENT class.

        turns_direction = Global.CurrentKeyboard[self.RIGHT] - Global.CurrentKeyboard[self.LEFT]
        moving_directions = Global.CurrentKeyboard[self.UP] - Global.CurrentKeyboard[self.DOWN]
        gun_turns_direction = Global.CurrentKeyboard[self.GUN_RIGHT] - Global.CurrentKeyboard[self.GUN_LEFT]

        if turns_direction or moving_directions or gun_turns_direction:
            Global.TankNetworkListenerConnection.Send({
                'action': Global.NetworkActions.TANK_MOVE,
                'pos': self.target.position,
                'turn': turns_direction,
                'mov': moving_directions,
                'gun_turn': gun_turns_direction,
                'time': time(),
                'id': self.target.id
            })

        if Global.CurrentKeyboard[self.FIRE_LIGHT_GUN]:
            self.target.fire()

        if Global.CurrentKeyboard[self.FIRE_HEAVY_GUN]:
            self.target.heavy_fire()