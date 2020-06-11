from microbit import *
from enum import *


class WIFI(object):
    """基本描述

    ESP8266 WI-FI模块AT固件

    """

    def __init__(self, RJ_pin):
        if RJ_pin == J1:
            # pass
            uart.init(tx=pin8, rx=pin1, baudrate=115200)
        elif RJ_pin == J2:
            uart.init(tx=pin12, rx=pin8, baudrate=115200)
        elif RJ_pin == J3:
            uart.init(tx=pin14, rx=pin13, baudrate=115200)
        elif RJ_pin == J4:
            uart.init(tx=pin16, rx=pin15, baudrate=115200)
        uart.write("AT+RESTORE" + "\r\n")
        sleep(100)
        uart.write("AT+CWMODE=1" + "\r\n")

    def __sendData(self, CMD):
        uart.write(CMD + "\r\n")
        time = running_time()
        uart_read_str = ""
        while True:
            uart_read_str += str(uart.read())
            if "OK" in uart_read_str:
                return True
            if running_time() - time > 5000:
                return False
            if len(uart_read_str) > 100:
                uart_read_str = ""

    def connectWIFI(self, SSID, password):
        """

        连接WI-FI，只支持2.4G网络

        Args:
            SSID (string): WI-FI名称
            password (string): WI-FI密码

        Returns:
            boolean: 执行是否成功
        """
        first_CMD = "AT+CWJAP=" + "\"" + SSID + "\",\"" + password + "\"\r\n"
        return self.__sendData(first_CMD)

    def connectThingSpeak(self):
        first_CMD = "AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",80"
        return self.__sendData(first_CMD)


if __name__ == '__main__':
    IoT = WIFI(J1)
    while True:
        if button_a.is_pressed():
            print(IoT.connectWIFI("ELECFREAKS_2.4G", "elecfreaks2019"))
        elif button_b.is_pressed():
            IoT.connectThingSpeak()
