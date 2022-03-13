"""sample_motors

This file serves as a list of example code using the motors. It is 
meant to be run with a Motor attached to Port MA. It uses 'input' calls
to let you stop execution for as long as you want, because any motor 
method (except "wait_*" methods) will simply jump to the next line of code 
after being executed. You usually use "busy-waiting" while loops to wait 
for a motor to be done rotating according to certain conditions.

Author: Ryan Au
January 24th, 2022
"""

### This file should be moved to the project/ folder if you want to run it ###

###########################
### Power-based Control ###
###########################

from utils.brick import Motor

theMotor = Motor("A")

theMotor.set_power(50)
print("theMotor.set_power(50)")
input("# Press any key to continue...")

# limits are used for position movement, not power movement
theMotor.set_limits(power=20)

theMotor.set_power(70) # increase to 70% instead of 20%
print("theMotor.set_power(70)")
input("# Press any key to continue...")

theMotor.set_power(0) # always do 0% to stop motor
print("theMotor.set_power(0)")
input("# Press any key to continue...")

# float_motor lets it move freely. 0% power resists movement.
theMotor.float_motor()
print("theMotor.float_motor()")
input("# Press any key to continue...")

##############################
### Position-based Control ###
##############################

from utils.brick import Motor
import time

theMotor = Motor("A")

# Set target speed first, 360 deg/sec
# Reset power limit to limitless with 0, default values:(power=0, dps=0)
theMotor.set_limits(dps=360)

# set current position to absolute pos 0deg
theMotor.reset_encoder()

# command to move to absolute pos 270deg
theMotor.set_position(270)
print("theMotor.set_position(270)")
input("# Press any key to continue...")

# command to rotate 90deg away from current position
theMotor.set_position_relative(90)
print("theMotor.set_position_relative(90)")
input("Press any key to continue...")

"""Tests 3 different speeds. set_dps overrides set_limits.
dps=180, rotation_dist=720
dps=360, rotation_dist=1080
dps=540, rotation_dist=1440
"""
for i, speed in enumerate([180, 360, 180*3]):
    theMotor.set_dps(speed) # overrides previous limits. Use limits or set_dps
    theMotor.set_position_relative(360 * (i+2))
    theMotor.wait_is_moving()
    while theMotor.is_moving():
        time.sleep(0.1)
        print("actual speed=", theMotor.get_dps(), "actual power=", theMotor.get_power(), "status=", theMotor.get_status())
