from utils.brick import EV3ColorSensor, TouchSensor, wait_ready_sensors
from utils.logging import log
import os

C = EV3ColorSensor(4)
T = TouchSensor(2)

wait_ready_sensors()

NAME = "COLOR SENSOR TEST"

if __name__ == "__main__":

    # Create the logging folder, and the log file.
    # Then we create the title.
    if not os.path.isdir("log"):
        os.mkdir("log")

    with open(open("log/color_sensor.csv", "a")) as l:
        l.write(",".join([
            "Red Value",
            "Green Value",
            "Blue Value",
            "Intensity",
            "Red Normalized",
            "Green Normalized",
            "Blue Normalized"
        ]))

        while True:

            # Log one shot.
            if T.is_pressed():
                while T.is_pressed():
                    pass
                readings = C.get_value()
                if readings is None or sum(readings[:3]) == 0:
                    continue
                s = sum(readings[:3])
                normalized_values = [
                    readings[0] / s,
                    readings[1] / s,
                    readings[2] / s
                ]
                total_data = readings + normalized_values
                log("----------START!----------", NAME)
                log(f"R: {readings[0]} G: {readings[1]} B: {readings[2]} I: {readings[3]}", NAME)
                log(
                    f"NR: {normalized_values[0]} NG: {normalized_values[1]} NB: {normalized_values[2]}", NAME)
                log("-------DONE Y(^_^)Y-------", NAME)
                l.write("\n" + ",".join(list(map(lambda i: str(i), total_data))))
