#!/usr/bin/env python3

# TODO Add more details about your overall shoe retrieval system implementation in the docstring below
"""
Retrieve foam cubes given a certain color.
"""

# Adjust these imports based on your implementation
#from logic import get_bin_for_color
from utils.brick import Motor, wait_ready_sensors, EV3ColorSensor, TouchSensor
import time
from pistonControls import Controls
from colorDetection import ColorRecognition


# Initialize hardware devices here 
RP, GP, BP = Motor.create_motors("ABC")
C = EV3ColorSensor(1) # port S2
T = TouchSensor(2)

wait_ready_sensors()

RP.reset_encoder()
RP.set_limits(power=80)
RP.set_limits(dps=2050)

GP.reset_encoder()
GP.set_limits(power=80)
GP.set_limits(dps=2050)

BP.reset_encoder()
BP.set_limits(power=80)
BP.set_limits(dps=2050)

# limits are used for position movement, not power movement
def main():
    flag = False

    while not flag:
        if T.is_pressed():
            while T.is_pressed():
                pass
            flag = True
        while flag:
            reading = C.get_value()
            if reading != None:
                print(reading)
                color = ColorRecognition.detectColor(reading[0], reading[1], reading[2])
                if color != None:
                    print(color)
                    if color != "None":
                        if color == "Red":
                            print("here")
                            Controls.pushCube(RP)
                            print("extend")
                        elif color == "Green":
                            Controls.pushCube(GP)
                        elif color == "Blue":
                            Controls.pushCube(BP)
            if T.is_pressed():
                while T.is_pressed():
                    pass
                flag = False

    Controls.resetMotors([RP, GP, BP])
    
        


# Define your classes and functions here. Consider using other files if this one gets too large
    

if __name__ == "__main__":
    print("Starting shoe retrieval system...")
    main()