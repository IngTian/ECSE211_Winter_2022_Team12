from utils.brick import Motor
import time

EXTEND = -300
RETRACT = 300
STARTING = 0
PISTONPAUSE = 0.5

class Controls:
    @staticmethod
    def pushCube(motor):
        motor.set_position(EXTEND)
        motor.wait_is_moving()
        motor.wait_is_stopped()
        motor.set_position(0)
        motor.wait_is_moving()
        motor.wait_is_stopped()
        return

    @staticmethod
    def resetMotors(motors):
        for m in motors:
            m.set_position(STARTING)
        time.sleep(1.5)
        return