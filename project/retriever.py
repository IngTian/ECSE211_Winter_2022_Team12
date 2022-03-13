#!/usr/bin/env python3

# TODO Add more details about your overall shoe retrieval system implementation in the docstring below
"""
Retrieve foam cubes given a certain color.
"""

# Adjust these imports based on your implementation
#from logic import get_bin_for_color
from utils.brick import Motor
import time


# Initialize hardware devices here 
m = Motor("A")
m.reset_encoder()
m.set_limits(power=80)
m.set_limits(dps=360)

# limits are used for position movement, not power movement
def main():
    m.set_position(-300)
    while(input("here") != "bye"):
        pass
    m.set_position(0)
    time.sleep(2)
    
        


# Define your classes and functions here. Consider using other files if this one gets too large
    

if __name__ == "__main__":
    print("Starting shoe retrieval system...")
    main()