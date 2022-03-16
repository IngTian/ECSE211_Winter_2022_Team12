from utils.brick import EV3ColorSensor
from enum import Enum
from utils.logging import log


class Color(Enum):
    RED = 1,
    GREEN = 2,
    BLUE = 3,
    UNIDENTIFIED = 4

COMPONENT_NAME = 'Color Sensor'
class ColorDetectionUnit:

    def __init__(self, port: int) -> None:
        self.color_sensor: EV3ColorSensor = EV3ColorSensor(port)

    def detect_color(self) -> Color:
        readings = self.color_sensor.get_value()
        log("COLOR: " + str(readings), COMPONENT_NAME)
        red, green, blue = readings
        if red < 270 and red >= 220 and green < 40 and green >= 20 and blue < 30 and blue >= 10:
            return Color.RED
        elif red < 35 and red >= 20 and green < 135 and green >= 110 and blue < 35 and blue >= 15:
            return Color.GREEN
        elif red < 45 and red >= 15 and green < 60 and green >= 40 and blue < 55 and blue >= 40:
            return Color.BLUE
        else:
            return Color.UNIDENTIFIED
