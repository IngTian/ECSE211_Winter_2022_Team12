#!/usr/bin/env python3
"""
This file sorts the color foams into various
color bins. 

Concretely, the client can initiate the sorting
process by pressing on the touch sensor. Then, 
When the color foam falls on the platform 
from the container funnel, the color
sensor underneath the platform shall read the
color of the cube. Next, the cube ejection
unit is going to push the color tube into
corresponding color bins. Currently, we
only allow for 3 colors: red, green, and blue.
"""

# Adjust these imports based on your implementation
#from logic import get_bin_for_color
from utils.brick import wait_ready_sensors, TouchSensor
from utils.logging import log
import time
from components.cube_ejection_unit import CubeEjectionUnit
from components.color_detection_unit import ColorDetectionUnit, Color

# Initiate Hardware Devices, i.e.,
# the cube ejection unit, the color
# sensor, and the touch sensor.
RP = CubeEjectionUnit("A")
GP = CubeEjectionUnit("B")
BP = CubeEjectionUnit("C")
C = ColorDetectionUnit(1)
T = TouchSensor(2)

wait_ready_sensors()
RP.set_state()
GP.set_state()
BP.set_state()

SUBSYSTEM_NAME = "Sorter"


if __name__ == "__main__":
    log("The sorter has started.", SUBSYSTEM_NAME)
    flag = False

    while not flag:
        if T.is_pressed():
            while T.is_pressed():
                pass
            flag = True
            log("The sorting process begins.", SUBSYSTEM_NAME)

        while flag:
            color: Color = C.detect_color()
            if color is not None and color != Color.UNIDENTIFIED:
                if color == Color.RED:
                    log("Detected red cube......pushing", SUBSYSTEM_NAME)
                    RP.push_cube()
                elif color == Color.GREEN:
                    log("Detected green cube......pushing", SUBSYSTEM_NAME)
                    GP.push_cube()
                elif color == Color.BLUE:
                    log("Detected blue cube......pushing", SUBSYSTEM_NAME)
                    BP.push_cube()
            
            # If we detect another touch,
            # we simply terminate the program.
            if T.is_pressed():
                while T.is_pressed():
                    pass
                flag = False

    CubeEjectionUnit.reset_motors([RP, GP, BP])