from microbit import *
from enum import *
import utime


class DS18B20(object):
    """基本描述

    水位传感器，返回0-100百分比

    Args:
        RJ_pin (pin): 连接端口

    Returns:
        value: 水位百分比
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

    def __init_18b20(self):
        self.__pin.write_digital(1)
        utime.sleep_us(30)
        self.__pin.write_digital(0)
        utime.sleep_us(600)
        self.__pin.write_digital(1)
        utime.sleep_us(30)
        __ack = self.__pin.read_digital()
        utime.sleep_us(600)
        self.__pin.write_digital(1)
        return __ack

    def __write_18b20(self, data):
        sc_byte = 0x01
        for i in range(0, 8):
            self.__pin.write_digital(0)
            utime.sleep_us(15)
            if data & sc_byte:
                self.__pin.write_digital(1)
                utime.sleep_us(45)
            else:
                self.__pin.write_digital(0)
                utime.sleep_us(45)
            self.__pin.write_digital(1)
            data = data >> 1

    def __read_18b20(self):
        dat = 0x00
        sc_byte = 0x01
        for i in range(0, 8):
            self.__pin.write_digital(1)
            utime.sleep_us(2)
            self.__pin.write_digital(0)
            utime.sleep_us(3)
            self.__pin.write_digital(1)
            utime.sleep_us(5)
            if self.__pin.read_digital():
                dat = dat + sc_byte
            sc_byte = sc_byte << 1
            utime.sleep_us(60)
        return dat

    def get_temperature(self):
        """

        读取摄氏温度 C

        """
        self.__init_18b20()
        self.__write_18b20(0xCC)
        self.__write_18b20(0x44)
        self.__init_18b20()
        self.__write_18b20(0xCC)
        self.__write_18b20(0xBE)
        low = self.__read_18b20()
        high = self.__read_18b20()
        print("high", high)
        print("low", low)
        temp = high << 8 | low
        temp = temp / 16
        if temp > 130:
            return None
        return temp


if __name__ == "__main__":
    s = DS18B20(J2)
    while True:
        print(s.get_temperature())
