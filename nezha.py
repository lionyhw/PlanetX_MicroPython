from microbit import *

J1 = pin8
J2 = pin12
J3 = pin14
J4 = pin16

NEZHA_ADDR = 0x10


class NEZHA(object):
    """基本描述

    哪吒RJ11主控板

    """
    def __init__(self):
        i2c.init()

    def set_motors(self, motor, speed):
        """基本描述

        选择电机并且设置速度

        Args:
            motor (number): 选择第几个电机,1,2,3,4
            speed (number): 设置电机速度 -100~100
        """
        if speed > 100 or speed < -100:
            raise ValueError('speed error,-100~100')
        if motor > 4 or motor < 1:
            raise ValueError('select motor error,1,2,3,4')
        if speed < 0:
            i2c.write(NEZHA_ADDR, bytearray([motor, 0x02, speed * -1, 0]))
        else:
            i2c.write(NEZHA_ADDR, bytearray([motor, 0x01, speed, 0]))

    def set_servo(self, servo, angle):
        """基本描述

        选择电机并且设置速度

        Args:
            servo (number): 选择第几个舵机（伺服电机）,1,2,3,4
            angle (number): 设置舵机角度 -100~100
        """
        if servo > 4 or servo < 1:
            raise ValueError('select servo error,1,2,3,4')
        if angle > 180 or angle < 0:
            raise ValueError('angle error,0~180')
        if servo == 1:
            i2c.write(NEZHA_ADDR, bytearray([0x10, angle, 0, 0]))
        elif servo == 2:
            i2c.write(NEZHA_ADDR, bytearray([0x11, angle, 0, 0]))
        elif servo == 3:
            i2c.write(NEZHA_ADDR, bytearray([0x12, angle, 0, 0]))
        elif servo == 4:
            i2c.write(NEZHA_ADDR, bytearray([0x13, angle, 0, 0]))


if __name__ == '__main__':
    nezha = NEZHA()

    nezha.set_motors(1, 100)
    nezha.set_servo(1, 90)
