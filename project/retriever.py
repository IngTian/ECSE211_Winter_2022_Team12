#!/usr/bin/env python3
"""
This subsystem is responsible for delivering the
requested color foam into the delivery area.

Concretely, this subsystem shall be initiated by
a press on the touch sensor. Then it shall wait for the readings
from the color sensor. If the reading is stable for a period.
Then, this subsystem shall command the corresponding cube 
ejection unit to push the requested cube into the hole. 
"""

# Adjust these imports based on your implementation
#from logic import get_bin_for_color
from utils.brick import wait_ready_sensors, TouchSensor, Motor
from utils.logging import log
from config import PISTON_DELIVERY
from components.cube_ejection_unit import CubeEjectionUnit
from components.color_detection_unit import ColorDetectionUnit, Color

# Initiate Hardware Devices, i.e.,
# the cube ejection unit, the color
# sensor, and the touch sensor.
RP = CubeEjectionUnit("A", config=PISTON_DELIVERY)
GP = CubeEjectionUnit("B", config=PISTON_DELIVERY)
BP = CubeEjectionUnit("C", config=PISTON_DELIVERY)
CONVEYER_BELT = Motor("D", config=PISTON_DELIVERY)

C = ColorDetectionUnit(4)
T = TouchSensor(2)

# Wait for hardwares to initialize.
wait_ready_sensors()

RP.set_state()
GP.set_state()
BP.set_state()
CONVEYER_BELT.reset_encoder()
CONVEYER_BELT.set_limits(dps=2050, power=80)

SUBSYSTEM_NAME = "Deliver"


if __name__ == "__main__":
    log("The deliver has started.", SUBSYSTEM_NAME)
    log("The delivery process begins.", SUBSYSTEM_NAME)
    CONVEYER_BELT.set_dps(360)

    while True:
        color: Color = C.detect_color()

        if T.is_pressed():
            if color is not None and color != Color.UNIDENTIFIED:
                if color == Color.RED:
                    log("Detected red cube......releasing", SUBSYSTEM_NAME)
                    RP.push_cube()
                elif color == Color.GREEN:
                    log("Detected green cube......releasing", SUBSYSTEM_NAME)
                    GP.push_cube()
                elif color == Color.BLUE:
                    log("Detected blue cube......releasing", SUBSYSTEM_NAME)
                    BP.push_cube()
