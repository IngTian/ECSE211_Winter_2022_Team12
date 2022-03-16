from utils.brick import Motor
from typing import List
import time
from config import PISTON

EXTEND = PISTON["EXTENDING_POSITION"]
RETRACT = PISTON["RETRACT_POSITION"]
STARTING = PISTON["RESET_POSITION"]
PISTON_PAUSE = PISTON["PISTON_PAUSE"]


class CubeEjectionUnit:

    def __init__(self, port: str) -> None:
        self.motor: Motor = Motor.create_motors(port)
        self.motor.reset_encoder()
        self.motor.set_limits(
            dps=PISTON['SPEED_LIMIT'], power=PISTON['POWER_LIMIT'])

    def push_cube(self) -> None:
        self.motor.set_position(EXTEND)
        self.motor.wait_is_moving()
        self.motor.wait_is_stopped()
        self.motor.set_position(0)
        self.motor.wait_is_moving()
        self.motor.wait_is_stopped()
        return

    @staticmethod
    def reset_motors(motors: List[Motor]) -> None:
        for m in motors:
            m.set_position(STARTING)
        time.sleep(1.5)
        return
