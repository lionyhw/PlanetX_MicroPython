from microbit import *
from enum import *


class DUST(object):
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
            self.__pin_vo = pin1
            self.__pin_vLED = pin8
        elif RJ_pin == J2:
            self.__pin_vo = pin2
            self.__pin_vLED = pin12

    def get_dust(self):
        """基本描述

        读取距离值

        Args:
            unit (number): 检测距离单位 0 厘米 1 英尺

        Returns:
            distance: 距离
        """
        __voltage = 0
        __dust = 0
        self.__pin_vLED.write_digital(0)
#        control.waitMicros(160);
        sleep(160)
#        voltage = pins.analogReadPin(vo);
        __voltage = self.__pin_vo.read_analog()
#        control.waitMicros(100);
        sleep(100)
#        pins.digitalWritePin(vLED, 1);
        self.__pin_vLED.write_digital(1)
#        voltage = pins.map(
#            voltage,
#            0,
#            1023,
#            0,
#            Reference_VOLTAGE / 2 * 3
#        );
#        dust = (voltage - 380) * 5 / 29;
#        if (dust < 0) {
#            dust = 0
#        }
#        return Math.round(dust)


if __name__ == "__main__":
    dis = DISTANCE(J1)
    while 1:
        print(dis.get_distance())
        sleep(500)
