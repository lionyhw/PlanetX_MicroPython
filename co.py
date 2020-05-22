from microbit import *
from enum import *


class CO(object):
    """基本描述

    一氧化碳传感器

    Args:
        RJ_pin (pin): 连接端口

    Returns:
        value: 一氧化碳值
    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pin = pin1
        elif RJ_pin == J2:
            self.__pin = pin2

    def get_co(self):
        """基本描述

        获取一氧化碳值

        """
        return self.__pin.read_analog()


if __name__ == '__main__':
    co = CO()
    while True:
        print(co.get_co())
