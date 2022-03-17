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
        s = sum(readings[:3])
        red, green, blue = readings[0] / s, readings[1] / s, readings[2] / s
        if red >= 0.9:
            return Color.RED
        elif green >= 0.9:
            return Color.GREEN
        elif blue >= 0.9:
            return Color.BLUE
        else:
            return Color.UNIDENTIFIED
