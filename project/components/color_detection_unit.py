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
        if readings is None:
            return Color.UNIDENTIFIED

        red, green, blue = readings[0], readings[1], readings[2]

        if red < 255 and red >= 220 and green < 40 and green >= 20 and blue < 30 and blue >= 10:
            return Color.RED
        elif red < 35 and red >= 215 and green < 135 and green >= 120 and blue < 30 and blue >= 10:
            return Color.GREEN
        elif red < 30 and red >= 15 and green < 50 and green >= 35 and blue < 60 and blue >= 45:
            return Color.BLUE
        else:
            return Color.UNIDENTIFIED
