from microbit import *
from enum import *


class BUTTON(object):
    """基本描述

    AB 按钮

    Args:
        RJ_pin (pin): 连接端口

    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            self.__pinA = pin1
            self.__pinB = pin8
        elif RJ_pin == J2:
            self.__pinA = pin2
            self.__pinB = pin12
        elif RJ_pin == J3:
            self.__pinA = pin13
            self.__pinB = pin14
        elif RJ_pin == J4:
            self.__pinA = pin15
            self.__pinB = pin16

        self.__pinA.set_pull(self.__pinA.PULL_UP)
        self.__pinB.set_pull(self.__pinB.PULL_UP)

    def A_is_pressed(self) -> bool:
        """基本描述

        判断A按钮按下

        Returns:
            boolean: 按下返回True, 未按下返回False

        """
        if self.__pinA.read_digital() == 0 and self.__pinB.read_digital() == 1:
            return True
        else:
            return False

    def B_is_pressed(self) -> bool:
        """基本描述

        判断A按钮按下

        Returns:
            boolean: 按下返回True, 未按下返回False

        """
        if self.__pinB.read_digital() == 0 and self.__pinA.read_digital() == 1:
            return True
        else:
            return False

    def AB_is_pressed(self) -> bool:
        """基本描述

        判断AB按钮同时按下

        Returns:
            boolean: 按下返回True, 未按下返回False

        """
        if self.__pinB.read_digital() == 0 and self.__pinA.read_digital() == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    button = BUTTON(J1)
    while True:
        if button.A_is_pressed():
            display.show(Image.HAPPY)
        elif button.B_is_pressed():
            display.show(Image.SAD)
        elif button.AB_is_pressed():
            display.show(Image.COW)
