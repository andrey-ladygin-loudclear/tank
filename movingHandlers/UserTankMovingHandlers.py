import operator

from components import Global
from movingHandlers.DefaultTankMovingHandlers import DefaultTankMovingHandlers
from pyglet.window import key


class UserTankMovingHandlers(DefaultTankMovingHandlers):

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
        super(UserTankMovingHandlers, self).step(dt) # Run step function on the parent class.

        turns_direction = Global.CurrentKeyboard[self.RIGHT] - Global.CurrentKeyboard[self.LEFT]
        moving_directions = Global.CurrentKeyboard[self.UP] - Global.CurrentKeyboard[self.DOWN]
        gun_turns_direction = Global.CurrentKeyboard[self.GUN_RIGHT] - Global.CurrentKeyboard[self.GUN_LEFT]

        if Global.CurrentKeyboard[self.FIRE_LIGHT_GUN]:
            self.target.fire()

        if Global.CurrentKeyboard[self.FIRE_HEAVY_GUN]:
            self.target.heavy_fire()

        self.addSpeed(moving_directions)

        # Set the object's velocity.
        self.setTankRotation(turns_direction, moving_directions)
        new_velocity = self.getVelocity()

        new_position = tuple(map(operator.add, self.target.position, new_velocity))

        if self.checkCollisionsWithObjects():
            self.target.velocity = (0, 0)
            self.target.position = self.target.old_position
        else:
            self.target.old_position = self.target.position
            new_velocity = self.getVelocityByNewPosition(self.target.position, new_position)
            self.setNewVelocity(new_velocity)


        # SHOULD REDUCE SPEED IF NEXT POSITION IS WALL
        #self.setNewVelocity(new_velocity)
        self.setGunPosition()

        # Set the object's rotation
        self.setGunRotation(gun_turns_direction)