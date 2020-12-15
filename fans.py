from microbit import *
from enum import *


class FANS(object):
    """基本描述

    设置风扇运动模式

    Args:
        RJ_pin (pin): 连接端口

    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pin = pin1
        elif RJ_pin == J2:
            self.__pin = pin2
        elif RJ_pin == J3:
            self.__pin = pin13
        elif RJ_pin == J3:
            self.__pin = pin15

    def set_fans(self, state, speed=100):
        """基本描述

        启动或者停止电机

        Args:
            state (numbers): 1运转 0停止
            speed (numbers): 速度百分比，state为1时使能 0-100

        """
        if state == 0:
            self.__pin.write_analog(0)
        elif state == 1:
            speed = ((speed - 0) * (1023 - 0)) / (100 - 0) + 0;
            self.__pin.write_analog(speed)
        else:
            print("speed error,must 0 <= brightness <= 100")


if __name__ == "__main__":
    f = FANS(J1)
    f.set_fans(1, 80)
