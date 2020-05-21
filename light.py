from microbit import *
from enum import *


class LIGHT(object):
    """基本描述

    环境光传感器，返回lux

    Args:
        RJ_pin (pin): 连接端口

    Returns:
        value: 光线强度 0-16000lux
    """
    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pin = pin1
        elif RJ_pin == J2:
            self.__pin = pin2

    def get_lightlevel(self):
        """基本描述

        环境光传感器，返回lux

        Returns:
            value: 光强度单位勒克司Lux
        """
        __value = self.__pin.read_analog()
        if __value <= 200:
            return ((__value - 43) * (1600 - 0)) / (200 - 43) + 0
        else:
            return ((__value - 200) * (14000 - 1600)) / (1023 - 200) + 1600


if __name__ == "__main__":
    s = LIGHT(J1)
    while True:
        print(s.get_lightlevel())
