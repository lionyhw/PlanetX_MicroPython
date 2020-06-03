from microbit import *
from time import sleep_us
from machine import time_pulse_us
from enum import *


class DISTANCE(object):
    """基本描述

    HC_SR04超声波支持库，可以选择返回厘米和英尺

    Args:
        pin_trig (pin): Trig信号引脚
        pin_echo (pin): Echo信号引脚

    Returns:
        distance: 距离
    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pin_e = pin8
            self.__pin_t = pin1
        elif RJ_pin == J2:
            self.__pin_e = pin12
            self.__pin_t = pin2
        elif RJ_pin == J3:
            self.__pin_e = pin14
            self.__pin_t = pin13
        elif RJ_pin == J4:
            self.__pin_e = pin16
            self.__pin_t = pin15

    def get_distance(self, unit=0):
        """基本描述

        读取距离值

        Args:
            unit (number): 检测距离单位 0 厘米 1 英尺

        Returns:
            distance: 距离
        """
        self.__pin_e.read_digital()
        self.__pin_t.write_digital(1)
        sleep_us(10)
        self.__pin_t.write_digital(0)
        ts = time_pulse_us(self.__pin_e, 1, 25000)

        distance = ts * 9 / 6 / 58
        if unit == 0:
            return distance
        elif unit == 1:
            return distance / 254


if __name__ == "__main__":
    dis = DISTANCE(J1)
    while 1:
        print(dis.get_distance())
        sleep(500)
