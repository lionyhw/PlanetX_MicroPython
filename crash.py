from microbit import *
from enum import *


class CRASH(object):
    """基本描述

    碰撞传感器

    Args:
        RJ_pin (pin): 连接端口

    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pin = pin8
        elif RJ_pin == J2:
            self.__pin = pin12
        elif RJ_pin == J3:
            self.__pin = pin14
        elif RJ_pin == J4:
            self.__pin = pin16

        self.__pin.set_pull(self.__pin.PULL_UP)

    def crash_is_pressed(self) -> bool:
        """基本描述

        碰撞传感器被按下

        Returns:
            boolean: 按下返回True, 未按下返回False

        """
        if self.__pin.read_digital() == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    button = CRASH(J1)
    while True:
        if button.crash_is_pressed():
            display.show(Image.HAPPY)
        else:
            display.show(Image.SAD)
