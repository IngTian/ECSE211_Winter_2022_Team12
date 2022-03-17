from utils.brick import Motor, wait_ready_sensors
from typing import List
import time
from config import PISTON

class CubeEjectionUnit:

    def __init__(self, port: str, config = PISTON) -> None:
        self.motor: Motor = Motor(port)
        self.EXTEND = config["EXTENDING_POSITION"]
        self.RETRACT = config["RETRACT_POSITION"]
        self.STARTING = config["RESET_POSITION"]
        self.PISTON_PAUSE = config["PISTON_PAUSE"]

    def set_state(self):
        self.motor.reset_encoder()
        self.motor.set_limits(
            dps=PISTON['SPEED_LIMIT'], power=PISTON['POWER_LIMIT'])

    def push_cube(self) -> None:
        self.motor.set_position(self.EXTEND)
        self.motor.wait_is_moving()
        self.motor.wait_is_stopped()
        self.motor.set_position(0)
        self.motor.wait_is_moving()
        self.motor.wait_is_stopped()
        return

    @staticmethod
    def reset_motors(motors: List[Motor]) -> None:
        for m in motors:
            m.set_position(PISTON["RESET_POSITION"])
        time.sleep(1.5)
        return
