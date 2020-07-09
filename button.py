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
            self.__pinC = pin1
            self.__pinD = pin8
        elif RJ_pin == J2:
            self.__pinC = pin2
            self.__pinD = pin12
        elif RJ_pin == J3:
            self.__pinC = pin13
            self.__pinD = pin14
        elif RJ_pin == J4:
            self.__pinC = pin15
            self.__pinD = pin16

        self.__pinC.set_pull(self.__pinC.PULL_UP)
        self.__pinD.set_pull(self.__pinD.PULL_UP)

    def C_is_pressed(self) -> bool:
        """基本描述

        判断C按钮按下

        Returns:
            boolean: 按下返回True, 未按下返回False

        """
        if self.__pinC.read_digital() == 0 and self.__pinD.read_digital() == 1:
            return True
        else:
            return False

    def D_is_pressed(self) -> bool:
        """基本描述

        判断D按钮按下

        Returns:
            boolean: 按下返回True, 未按下返回False

        """
        if self.__pinD.read_digital() == 0 and self.__pinC.read_digital() == 1:
            return True
        else:
            return False

    def CD_is_pressed(self) -> bool:
        """基本描述

        判断CD按钮同时按下

        Returns:
            boolean: 按下返回True, 未按下返回False

        """
        if self.__pinD.read_digital() == 0 and self.__pinC.read_digital() == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    button = BUTTON(J1)
    while True:
        if button.C_is_pressed():
            display.show(Image.HAPPY)
        elif button.D_is_pressed():
            display.show(Image.SAD)
        elif button.CD_is_pressed():
            display.show(Image.COW)
