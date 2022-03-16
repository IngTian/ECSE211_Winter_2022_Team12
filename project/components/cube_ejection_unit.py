from utils.brick import Motor
from typing import List
import time
import config

EXTEND = config.PISTON["EXTENDING_POSITION"]
RETRACT = config.PISTON["RETRACT_POSITION"]
STARTING = config.PISTON["RESET_POSITION"]
PISTON_PAUSE = config.PISTON["PISTON_PAUSE"]

class PistonControls:
    @staticmethod
    def push_cube(motor: Motor):
        motor.set_position(EXTEND)
        motor.wait_is_moving()
        motor.wait_is_stopped()
        motor.set_position(0)
        motor.wait_is_moving()
        motor.wait_is_stopped()
        return

    @staticmethod
    def reset_motors(motors: List[Motor]):
        for m in motors:
            m.set_position(STARTING)
        time.sleep(1.5)
        return