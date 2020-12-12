from microbit import *
from enum import *


class MQ3(object):
    """基本描述

    MQ3酒精传感器

    Args:
        RJ_pin (pin): 连接端口

    Returns:
        value: 酒精值
    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pin = pin1
        elif RJ_pin == J2:
            self.__pin = pin2

    def get_smoke(self):
        """基本描述

        获取酒精值

        """
        return self.__pin.read_analog()


if __name__ == '__main__':
    co = MQ3()
    while True:
        print(co.get_smoke())
